import csv
import json
from pathlib import Path

MAPA_MEDICIONES = {
    "temperatura": "temperatura",
    "humedad": "humedad",
    "presion": "presion",
    "viento": "velocidad_viento",
    "velocidad_viento": "velocidad_viento",
    "direccion_viento": "direccion_viento",
}


def cargar_json(ruta_json):
    ruta = Path(ruta_json)
    if not ruta.exists():
        raise FileNotFoundError(f"El archivo JSON especificado no existe: '{ruta_json}'")
    with open(ruta, "r") as archivo:
        contenido = json.load(archivo)
    if isinstance(contenido, dict) and "registros_validos" in contenido:
        return contenido["registros_validos"]
    elif isinstance(contenido, list):
        return contenido
    else:
        raise ValueError("Formato de JSON no válido o sin campo 'registros_validos'.")


def filtrar_datos(datos, estacion, medicion):
    medicion_limpia = medicion.strip().lower()
    campo_medicion = MAPA_MEDICIONES.get(medicion_limpia, medicion_limpia)
    estacion_normalizada = estacion.strip().upper()
    filtrados = []
    
    for reg in datos:
        estacion_registro = reg.get("estacion", "").strip().upper()
        if estacion_registro == estacion_normalizada and campo_medicion in reg:
            filtrados.append(reg)
    return filtrados, campo_medicion


def exportar_csv(filtrados, ruta_csv):
    if not filtrados:
        return

    ruta = Path(ruta_csv)
    ruta.parent.mkdir(parents=True, exist_ok=True)

    encabezados = list(filtrados[0].keys())

    with open(ruta, "w") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=encabezados)
        writer.writeheader()
        writer.writerows(filtrados)