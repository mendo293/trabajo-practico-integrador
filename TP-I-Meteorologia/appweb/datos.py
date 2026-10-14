#1
import csv
import json
from pathlib import Path


def cargar_json(ruta_json):
    ruta = Path(ruta_json)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el archivo: '{ruta_json}'")

    with open(ruta, "r") as archivo:
        contenido = json.load(archivo)

    if isinstance(contenido, dict) and "registros_validos" in contenido:
        return contenido["registros_validos"] 
    else:
        return contenido


def obtener_estaciones(datos):
    estaciones = []

    for reg in datos: 
        if "estacion" in reg:
            nombre = reg["estacion"].strip().upper()
            if nombre != "" and nombre not in estaciones:
                estaciones.append(nombre)

    estaciones.sort() 
    return estaciones


def filtrar_datos(datos, estacion, medicion):
    campo = medicion.strip().lower()
    if campo == "viento":
        campo = "velocidad_viento"

    estacion_buscada = estacion.strip().upper() 
    filtrados = []

    for reg in datos:
        if "estacion" in reg and campo in reg:
            estacion_reg = reg["estacion"].strip().upper()
            if estacion_reg == estacion_buscada:
                filtrados.append(reg)

    return filtrados, campo


def exportar_csv(filtrados, ruta_csv):
    if not filtrados:
        return

    ruta = Path(ruta_csv) 
    ruta.parent.mkdir(parents=True, exist_ok=True) 

    encabezados = list(filtrados[0].keys()) 

    with open(ruta, "w") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados) 
        escritor.writeheader()
        escritor.writerows(filtrados) 