# TP Integrador 1 - Parte 1: Conversor de TXT a JSON (SMN)

## Información del Proyecto

- **Materia:** Programación I - Comisión 3 - Ingeniería Electrónica y Telecomunicaciones
- **Fecha de Primera Entrega:** 31/08/2026
- **Fecha de Segunda Entrega:** 07/09/2026
- **Docente:** 
  - Linquiman Ventura, Lautaro Yamil
- **Nombre del grupo:** 
  - Los Calamares
- **Integrantes:** 
  - Calabresi, Luciana Calabresi
  - Mendoza Ruffin, Alan Michael

---

## Descripción

Este programa permite procesar archivos de datos provenientes del Servicio Meteorológico Nacional (SMN). Realiza la lectura, limpieza y validación línea por línea, separando los registros válidos de los inválidos y generando un archivo estructurado en formato `.json`.

---

## Forma de Ejecución

El programa se ejecuta desde la terminal pasando como primer argumento la ruta del archivo `.txt` de origen y como segundo argumento la ruta de destino del archivo `.json`.

```bash
python adaptar_datos.py datos/observaciones.txt datos/observaciones.json