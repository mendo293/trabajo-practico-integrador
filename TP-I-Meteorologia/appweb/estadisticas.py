#2
def calcular_estadisticas(filtrados, campo_medicion):
    if not filtrados:
        return {"cantidad": 0, "minimo": None, "maximo": None, "promedio": None}

    valores = []
    for reg in filtrados:
        if campo_medicion in reg:
            val = reg[campo_medicion]
            if val is not None:
                valores.append(val)

    if not valores:
        return {"cantidad": 0, "minimo": None, "maximo": None, "promedio": None}

    cantidad = len(valores)
    minimo = min(valores)
    maximo = max(valores)
    promedio = sum(valores) / cantidad

    return {
        "cantidad": cantidad,
        "minimo": minimo,
        "maximo": maximo,
        "promedio": round(promedio, 2),
    }