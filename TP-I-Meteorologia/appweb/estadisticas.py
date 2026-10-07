def calcular_estadisticas(filtrados, campo_medicion):
    if not filtrados:
        return {
            "cantidad": 0,
            "minimo": None,
            "maximo": None,
            "promedio": None,
        }
        
    valores = []
    
    for reg in filtrados:
        val = reg.get(campo_medicion)
        if val is not None and isinstance(val, (int, float)):
            valores.append(val)

    if not valores:
        return {
            "cantidad": 0,
            "minimo": None,
            "maximo": None,
            "promedio": None,
        }

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