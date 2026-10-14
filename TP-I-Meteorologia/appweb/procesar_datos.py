#4
from datetime import datetime
import sys

from datos import cargar_json, exportar_csv, filtrar_datos
from estadisticas import calcular_estadisticas
from graficos import generar_grafica

def main():
    if len(sys.argv) < 4:
        print("Uso: python procesar_datos.py <ruta_json> <estacion> <medicion>")
        sys.exit(1)

    ruta_json = sys.argv[1]
    estacion = sys.argv[2]
    medicion = sys.argv[3]

    datos = cargar_json(ruta_json) 
    filtrados, campo = filtrar_datos(datos, estacion, medicion)

    if not filtrados:
        print("No se encontraron registros.")
        sys.exit(1)

    stats = calcular_estadisticas(filtrados, campo)

    fecha_hoy = datetime.now().strftime("%Y-%m-%d") 
    estacion_slug = estacion.lower().replace(" ", "_") 
    medicion_slug = campo.lower().replace(" ", "_") 

    ruta_csv = f"salidas/{fecha_hoy}_{estacion_slug}_{medicion_slug}.csv" 
    ruta_png = f"salidas/{fecha_hoy}_{estacion_slug}_{medicion_slug}.png" 

    exportar_csv(filtrados, ruta_csv) 
    generar_grafica(filtrados, estacion, campo, ruta_png) 

    print("\n--- RESULTADOS ---") 
    print("Estación:", estacion)
    print("Medición:", campo)
    print("Estadísticas:", stats)
    print("CSV guardado en:", ruta_csv)
    print("PNG guardado en:", ruta_png)


if __name__ == "__main__": 
    main()