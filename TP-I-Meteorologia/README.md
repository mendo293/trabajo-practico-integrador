# TP Integrador 1 - Parte 2

## Información del Proyecto

- **Materia:** Programación I - Comisión 3 - Ingeniería Electrónica y Telecomunicaciones
- **Fecha de Primera Entrega:** 07/10/2026
- **Fecha de Segunda Entrega:** 14/10/2026
- **Docente:** 
  - Linquiman Ventura, Lautaro Yamil
- **Nombre del grupo:** 
  - Los Calamares
- **Integrantes:** 
  - Calabresi, Luciana Calabresi
  - Mendoza Ruffin, Alan Michael

---

# Etapa 1 - Procesamiento de Datos Meteorológicos

Este módulo procesa las observaciones meteorológicas en formato JSON (generadas en la Parte 1 del T.P.). En esta etapa del proyecto implementamos el procesamiento, análisis estadístico y visualización gráfica de datos meteorológicos obtenidos en formato JSON (generadas en la Parte 1 del T.P.), con el procesamiento mediante estructuras nativas de Python: listas y diccionarios, sin el uso de librerías de análisis de datos como Pandas.

## Ejecución desde la Terminal

Posicionarse en la carpeta `app_web` y ejecutar:

```bash
python procesar_datos.py datos/observaciones.json "AEROPARQUE AERO" temperatura