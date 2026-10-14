#5
from datetime import datetime
import sys 

import pandas as pd 
import streamlit as st 

from datos import cargar_json, exportar_csv, filtrar_datos, obtener_estaciones 
from estadisticas import calcular_estadisticas
from graficos import generar_grafica


def main():
    st.title("Explorador de Datos Meteorológicos")

    if len(sys.argv) > 1: 
        ruta_json = sys.argv[1]
    else:
        ruta_json = "datos/observaciones.json"
        
    try:
        datos = cargar_json(ruta_json) 
    except Exception as e:
        st.error(f"Error al cargar el archivo JSON: {e}")
        return

    estaciones = obtener_estaciones(datos)
    mediciones = ["Temperatura", "Humedad", "Presion", "Viento"]

    if not estaciones:
        st.error("No se encontraron estaciones en el archivo JSON.")
        return

    st.sidebar.header("Filtros")
    estacion_sel = st.sidebar.selectbox("Seleccionar Estación:", estaciones)
    medicion_sel = st.sidebar.selectbox("Seleccionar Medición:", mediciones)

    filtrados, campo = filtrar_datos(datos, estacion_sel, medicion_sel)

    if not filtrados:
        st.warning("No hay datos para la opción seleccionada.") 
        return

    stats = calcular_estadisticas(filtrados, campo)

    st.header(f"Estadísticas: {estacion_sel}")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Cantidad", stats["cantidad"])
    col2.metric("Mínimo", stats["minimo"])
    col3.metric("Máximo", stats["maximo"])
    col4.metric("Promedio", stats["promedio"])

    fecha_hoy = datetime.now().strftime("%Y-%m-%d") 
    estacion_slug = estacion_sel.lower().replace(" ", "_")
    medicion_slug = campo.lower().replace(" ", "_")

    ruta_csv = f"salidas/{fecha_hoy}_{estacion_slug}_{medicion_slug}.csv"
    ruta_png = f"salidas/{fecha_hoy}_{estacion_slug}_{medicion_slug}.png"

    exportar_csv(filtrados, ruta_csv)
    generar_grafica(filtrados, estacion_sel, campo, ruta_png)

    st.header("Gráfico")
    st.image(ruta_png)

    st.header("Tabla de Datos")
    df = pd.DataFrame(filtrados) 
    st.dataframe(df) 

if __name__ == "__main__":
    main()