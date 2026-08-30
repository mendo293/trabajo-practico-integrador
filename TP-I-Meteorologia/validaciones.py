def es_bisiesto(anio):
    return(anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def validar_fecha(fecha_texto):
    fecha_limpia = fecha_texto.strip()
    if len(fecha_limpia) != 8 or not fecha_limpia.isdigit():
        return False

    dia = int(fecha_limpia[:2])
    mes = int(fecha_limpia[2:4])
    anio = int(fecha_limpia[4:])

    if mes < 1 or mes > 12:
        return False

    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if es_bisiesto(anio):
        dias_por_mes[2] = 29

    if dia < 1 or dia > dias_por_mes[mes]:
        return False

    return True


def validar_hora(hora_texto):
    try:
        hora = int(hora_texto.strip())
        return 0 <= hora <= 23
    except ValueError:
        return False


def validar_humedad(humedad_texto):
    try:
        hum = int(humedad_texto.strip())
        return 0 <= hum <= 100
    except ValueError:
        return False


def validar_direccion_viento(dir_texto):
    try:
        dd = int(dir_texto.strip())
        return 0 <= dd <= 360
    except ValueError:
        return False


def validar_velocidad_viento(vel_texto):
    try:
        ff = int(vel_texto.strip())
        return ff >= 0
    except ValueError:
        return False


def validar_numero_general(valor_texto):
    try:
        float(valor_texto.strip())
        return True
    except ValueError:
        return False

def  validar_estacion(estacion_texto):
    return len(estacion_texto.strip()) > 0

def validar_registro_completo(linea):
    partes = linea.split()
    
    if len(partes) < 8:
        return False, f"La línea no tiene al menos 8 campos ({len(partes)} recibidos)."
    
    fecha, hora, temp, hum, pnm, dd, ff = partes[:7]
    nombre = " ".join(partes[7:])

    if not validar_fecha(fecha):
        return False, f"Fecha inválida: '{fecha.strip()}'"
    if not validar_hora(hora):
        return False, f"Hora inválida: '{hora.strip()}'"
    if not validar_numero_general(temp):
        return False, f"Temperatura no numérica: '{temp.strip()}'"
    if not validar_humedad(hum):
        return False, f"Humedad fuera de rango (0-100) o no numérica: '{hum.strip()}'"
    if not validar_numero_general(pnm):
        return False, f"Presión no numérica: '{pnm.strip()}'"
    if not validar_direccion_viento(dd):
        return False, f"Dirección de viento fuera de rango (0-360) o no numérica: '{dd.strip()}'"
    if not validar_velocidad_viento(ff):
        return False, f"Velocidad de viento negativa o no numérica: '{ff.strip()}'"
    if not validar_estacion(nombre):
        return False, "El nombre de la estación está vacío."

    registro_dict = {
        "fecha": fecha.strip(),
        "hora": int(hora.strip()),
        "temperatura": float(temp.strip()),
        "humedad": int(hum.strip()),
        "presion": float(pnm.strip()),
        "direccion_viento": int(dd.strip()),
        "velocidad_viento": int(ff.strip()),
        "estacion": nombre.strip()
    }                        
    return True, registro_dict