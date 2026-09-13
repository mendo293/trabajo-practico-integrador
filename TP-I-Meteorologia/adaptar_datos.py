import json
import os
import sys

from validaciones import validar_registro


def es_linea_encabezado(linea):
    linea_limpia = linea.strip()
    if not linea_limpia:
        return True
    if (
        linea_limpia.startswith("FECHA")
        or "[HOA]" in linea_limpia
        or "[°C]" in linea_limpia
    ):
        return True
    return False


def procesar_archivo_txt(ruta_entrada):
    validos = []
    invalidos = []

    try:
        with open(ruta_entrada, "r") as archivo:
            for linea in archivo:
                linea_texto = linea.strip()

                if es_linea_encabezado(linea_texto):
                    continue

                es_valido, resultado = validar_registro(linea_texto)

                if es_valido:
                    validos.append(resultado)
                else:
                    invalidos.append(
                        {"linea_original": linea_texto, "motivo": resultado}
                    )

    except FileNotFoundError:
        print(
            f"Error: No se encontro el archivo de entrada especificado: '{ruta_entrada}'"
        )
        sys.exit(1)
    except Exception as error:
        print(f"Error inesperado al intentar leer el archivo: {error}")
        sys.exit(1)

    return validos, invalidos


def guardar_json_salida(datos, ruta_salida):
    try:
        directorio = os.path.dirname(ruta_salida)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)

        with open(ruta_salida, "w") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        print(f"\n[ÉXITO] Archivo JSON generado correctamente en: '{ruta_salida}'")

    except PermissionError:
        print(
            f"Error: Permisos insuficientes para escribir en la ruta: '{ruta_salida}'"
        )
        sys.exit(1)
    except Exception as error:
        print(f"Error al escribir el archivo JSON de salida: {error}")
        sys.exit(1)


def main():
    try:
        ruta_entrada = sys.argv[1]
        ruta_salida = sys.argv[2]
    except IndexError:
        print("Error: Cantidad de argumentos invalida.")
        print("\nUso esperado:")
        print(
            "  python adaptar_datos.py <ruta_archivo_entrada.txt> <ruta_archivo_salida.json>"
        )
        print("\nEjemplo:")
        print("  python adaptar_datos.py datos/observaciones.txt datos/observaciones.json")
        sys.exit(1)

    print("--- Procesando Conversión TXT a JSON ---")
    print(f"Entrada: {ruta_entrada}")
    print(f"Salida:  {ruta_salida}")

    registros_validos, registros_invalidos = procesar_archivo_txt(ruta_entrada)
    total_registros = len(registros_validos) + len(registros_invalidos)

    estructura_json = {
        "informacion_general": {
            "cantidad_registros_totales": total_registros,
            "cantidad_registros_validos": len(registros_validos),
            "cantidad_registros_invalidos": len(registros_invalidos),
        },
        "registros_validos": registros_validos,
        "registros_invalidos": registros_invalidos,
    }

    guardar_json_salida(estructura_json, ruta_salida)

    print("\n================ RESUMEN DEL PROCESAMIENTO ================")
    print(f"  Total de registros leídos   : {total_registros}")
    print(f"  Registros válidos procesados : {len(registros_validos)}")
    print(f"  Registros inválidos / error  : {len(registros_invalidos)}")
    print("===========================================================")


if __name__ == "__main__":
    main()