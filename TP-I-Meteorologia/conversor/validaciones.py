from datetime import datetime


def validar_registro(linea):
    partes = linea.strip().split()

    if len(partes) < 8:
        return False, "Cantidad insuficiente de campos en el registro."

    fecha_str = partes[0]
    hora_str = partes[1]
    temp_str = partes[2]
    hum_str = partes[3]
    pnm_str = partes[4]
    dd_str = partes[5]
    ff_str = partes[6]
    nombre_estacion = " ".join(partes[7:])

    if not nombre_estacion.strip():
        return False, "El nombre de la estacion no puede estar vacio."

    try:
        fecha_obj = datetime.strptime(fecha_str, "%d%m%Y")
        fecha_formateada = fecha_obj.strftime("%d/%m/%Y")
    except ValueError:
        return (
            False,
            f"Fecha inexistente o formato incorrecto ('{fecha_str}'). Esperado DDMMYYYY.",
        )

    try:
        hora = int(hora_str)
        if hora < 0 or hora > 23:
            return False, f"Hora fuera del rango valido (0-23): {hora}."
    except ValueError:
        return False, f"La hora no es un valor entero numerico: '{hora_str}'."

    try:
        temperatura = float(temp_str)
    except ValueError:
        return False, f"La temperatura no es un valor numerico: '{temp_str}'."

    try:
        humedad = float(hum_str)
        if humedad < 0 or humedad > 100:
            return (
                False,
                f"Humedad fuera del rango permitido (0-100%): {humedad}.",
            )
    except ValueError:
        return False, f"La humedad no es un valor numerico: '{hum_str}'."

    try:
        presion = float(pnm_str)
    except ValueError:
        return False, f"La presion (PNM) no es un valor numerico: '{pnm_str}'."

    try:
        direccion_viento = float(dd_str)
        if direccion_viento < 0 or direccion_viento > 360:
            return (
                False,
                f"Direccion del viento fuera de rango (0-360 deg): {direccion_viento}.",
            )
    except ValueError:
        return (
            False,
            f"La direccion del viento no es un valor numerico: '{dd_str}'.",
        )

    try:
        velocidad_viento = float(ff_str)
        if velocidad_viento < 0:
            return (
                False,
                f"La velocidad del viento no puede ser negativa: {velocidad_viento}.",
            )
    except ValueError:
        return (
            False,
            f"La velocidad del viento no es un valor numerico: '{ff_str}'.",
        )

    registro_parseado = {
        "fecha": fecha_formateada,
        "hora": hora,
        "temperatura": temperatura,
        "humedad": humedad,
        "presion": presion,
        "direccion_viento": direccion_viento,
        "velocidad_viento": velocidad_viento,
        "estacion": nombre_estacion,
    }

    return True, registro_parseado