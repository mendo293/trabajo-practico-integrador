from datetime import datetime
from pathlib import Path
import sys

import pandas as pd
import streamlit as st

from datos import cargar_json, exportar_csv, filtrar_datos, obtener_estaciones
from estadisticas import calcular_estadisticas
from graficos import generar_grafica


def armar_ruta_salida(estacion, medicion, extension):
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    estacion_slug = estacion.lower().replace(" ", "_").replace("(", "").replace(")", "")
    medicion_slug = medicion.lower().replace(" ", "_")
    return f"salidas/{fecha_hoy}_{estacion_slug}_{medicion_slug}.{extension}"


def main():
    st.set_page_config(
        page_title="Visualizador Meteorológico",
        layout="wide",
    )

    st.title("Explorador de Datos Meteorológicos")
    st.write("Aplicación interactiva para consultar registros, estadísticas y gráficas de la red meteorológica.")

    if len(sys.argv) > 1:
        ruta_json = sys.argv[1]
    else:
        ruta_json = "datos/observaciones.json"

    try:
        datos = cargar_json(ruta_json)
    except Exception as e:
        st.error(f"Error al cargar el archivo de datos ('{ruta_json}'): {e}")
        st.info("Verificá que la ruta al archivo JSON sea correcta y que el archivo exista.")
        return

    estaciones_disponibles = obtener_estaciones(datos)
    mediciones_disponibles = ["Temperatura", "Humedad", "Presión", "Viento"]

    if not estaciones_disponibles:
        st.error("No se encontraron estaciones válidas dentro del archivo JSON.")
        return

    st.sidebar.header("Controles de Filtro")
    estacion_sel = st.sidebar.selectbox("Seleccione la Estación:", estaciones_disponibles)
    medicion_sel = st.sidebar.selectbox("Seleccione la Medición:", mediciones_disponibles)

    filtrados, campo_medicion = filtrar_datos(datos, estacion_sel, medicion_sel)

    if not filtrados:
        st.warning(f"No se encontraron registros para la estación **{estacion_sel}** y la medición **{medicion_sel}**.")
        return

    stats = calcular_estadisticas(filtrados, campo_medicion)

    st.header(f"Resumen Estadístico: {estacion_sel}")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Cantidad de Registros", stats["cantidad"])
    col2.metric("Mínimo", f"{stats['minimo']}")
    col3.metric("Máximo", f"{stats['maximo']}")
    col4.metric("Promedio", f"{stats['promedio']}")

    ruta_csv = armar_ruta_salida(estacion_sel, campo_medicion, "csv")
    ruta_png = armar_ruta_salida(estacion_sel, campo_medicion, "png")

    exportar_csv(filtrados, ruta_csv)
    generar_grafica(filtrados, estacion_sel, campo_medicion, ruta_png)

    st.header("Evolución Temporal")
    st.image(ruta_png, caption=f"Evolución de {campo_medicion.capitalize()} en {estacion_sel}", use_container_width=True)

    st.header("Tabla de Datos Filtrados")
    df_filtrados = pd.DataFrame(filtrados)
    st.dataframe(df_filtrados, use_container_width=True)

    st.success(f"Archivos exportados correctamente en la carpeta `salidas/` (`.csv` y `.png`).")


if __name__ == "__main__":
    main()