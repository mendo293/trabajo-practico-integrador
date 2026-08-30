import sys
import json
import os
from validaciones import validar_registro_completo

def procesar_archivo_txt(ruta_entrada):
    validos = []
    invalidos = []
    total_registros = 0 
    
    with open(ruta_entrada, "r") as archivo:
        lineas = archivo.readlines()
    
    lineas_procesadas = []
        
    for linea in lineas:
        linea_limpia = linea.strip()

        if not linea_limpia:
            continue
            
        partes = linea_limpia.split()
    
        if (
            partes [0].upper().startswith("FECHA")
            or "TEMP" in linea_limpia
            or partes[0].startswith('[')
        ):
            continue
        
        if not (partes[0].isdigit() and len(partes[0]) == 8):
            if lineas_procesadas:
                lineas_procesadas[-1] = (
                    lineas_procesadas[-1] + ' ' + linea_limpia
                )
            continue
        
        lineas_procesadas.append(linea_limpia)
        
    for linea_limpia in lineas_procesadas:
        total_registros += 1
        es_valido, resultado = validar_registro_completo(linea_limpia)
        
        if es_valido:
            validos.append(resultado)
        else:
            invalidos.append(
                {"linea_original": linea_limpia,
                 "error": resultado
                 }
            )
    return total_registros, validos, invalidos

def main():
    if len(sys.argv) < 3:
        print("Error en los argumentos.")
        print(
            "Uso correcto: python adaptar_datos.py <archivo_entrada.txt>"
            "<archivo_salida.json>"
        )
        return
    
    ruta_entrada = sys.argv [1]
    ruta_salida = sys.argv [2]
    
    if not os.path.exists(ruta_entrada):
        print(f"Error: El archivo de entrada '{ruta_entrada}' no existe.")
        return
    
    try:
        (
            total_registros,
            registros_validos,
            registros_invalidos
        ) = procesar_archivo_txt(ruta_entrada)
        
        datos_json = {
            "informacion_general" : {
                "cantidad_registros": total_registros,
                "cantidad_validos": len(registros_validos),
                "cantidad_invalidos": len(registros_invalidos)
            },
            "registros_validos": registros_validos,
            "registros_invalidos": registros_invalidos
        }
        
        with open(ruta_salida, "w") as archivo_out:
            json.dump(datos_json, archivo_out)
        
        print("=== PROCESAMIENTO FINALIZADO ===")
        print(f"Total de registros procesados: {total_registros}")
        print(f"Registros válidos: {len(registros_validos)}")
        print(f"Registros inválidos: {len(registros_invalidos)}")
        print(f"Archivo JSON generado en: {ruta_salida}")
    
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{ruta_entrada}'.")
    except Exception as error:
        print(f"Ocurrió un error inesperado: '{error}'.")
        
if __name__ == "__main__":
    main()