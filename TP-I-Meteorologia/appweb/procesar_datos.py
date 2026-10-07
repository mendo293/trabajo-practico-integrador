from datetime import datetime
from pathlib import Path
import sys

from datos import cargar_json, exportar_csv, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica


def armar_ruta_salida(estacion, medicion, extension):
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    estacion_final = (
        estacion.lower()
        .replace(" ", "_")
        .replace("(", "")
        .replace(")", "")
    )
    medicion_final = medicion.lower().replace(" ", "_")
    return f"salidas/{fecha_hoy}_{estacion_final}_{medicion_final}.{extension}"


def main():
    if len(sys.argv) < 4:
        print("Error: Argumentos insuficientes.")
        print("\nUso esperado:")
        print("  python procesar_datos.py <ruta_json> <estacion> <medicion>")
        print("\nEjemplo:")
        print('  python procesar_datos.py datos/observaciones.json "AEROPARQUE AERO" temperatura')
        sys.exit(1)

    ruta_json = sys.argv[1]
    estacion = sys.argv[2]
    medicion = sys.argv[3]

    try:
        datos = cargar_json(ruta_json)
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        sys.exit(1)

    filtrados, campo_medicion = filtrar_datos(datos, estacion, medicion)

    if not filtrados:
        print(f"Error: No se encontraron registros para la estación '{estacion}' y la medición '{medicion}'.")
        sys.exit(1)

    estadisticas = calcular_estadisticas(filtrados, campo_medicion)

    ruta_csv = armar_ruta_salida(estacion, campo_medicion, "csv")
    ruta_png = armar_ruta_salida(estacion, campo_medicion, "png")

    try:
        exportar_csv(filtrados, ruta_csv)
        generar_grafica(filtrados, estacion, campo_medicion, ruta_png)
    except Exception as e:
        print(f"Error al generar archivos de salida: {e}")
        sys.exit(1)

    print("\n================ ESTADÍSTICAS CALCULADAS ================")
    print(f"  Estación  : {estacion}")
    print(f"  Medición  : {campo_medicion}")
    print(f"  Cantidad  : {estadisticas['cantidad']}")
    print(f"  Mínimo    : {estadisticas['minimo']}")
    print(f"  Máximo    : {estadisticas['maximo']}")
    print(f"  Promedio  : {estadisticas['promedio']}")
    print("=========================================================\n")

    print(f"Primeros registros filtrados (mostrando {min(3, len(filtrados))} de {len(filtrados)}):")
    for reg in filtrados[:3]:
        print(f"  - Fecha: {reg['fecha']}, Hora: {reg['hora']}h, {campo_medicion}: {reg[campo_medicion]}")

    print(f"\n[ÉXITO] Archivo CSV guardado en : {ruta_csv}")
    print(f"[ÉXITO] Gráfica guardada en   : {ruta_png}")


if __name__ == "__main__":
    main()