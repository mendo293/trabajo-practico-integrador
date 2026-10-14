#3
from pathlib import Path
import matplotlib.pyplot as plt ##matplotlib es una biblioteca de Python diseñada para crear gráficos


def generar_grafica(filtrados, estacion, medicion, ruta_salida): #importamos listas creadas en datos y estadisticas.
    """Genera el gráfico PNG con Matplotlib."""
    if not filtrados:
        return "" #Si un campo no tiene valor, el grafico se encuentra vacio. Ej: Presion, temp, humedad, viento.

    ruta = Path(ruta_salida) #depositar aqui los graficos de la web
    ruta.parent.mkdir(parents=True, exist_ok=True) # mkdir es para crear directorios (carpetas), las validaciones de parents, exist_ok
    #funcionan para validar si la carpeta existe, si no existe mkdir la crea.

    etiquetas_tiempo = []
    valores = []

    for reg in filtrados:
        fecha = reg.get("fecha", "")##get tanto fechas validas, como vacias
        hora = reg.get("hora", "")##""
        etiquetas_tiempo.append(f"{fecha} {hora}h")
        valores.append(reg[medicion]) #agrega fecha y hora en las madiciones correspondientes. o sea, los graficos los en base a los tipos de mediciones.

    plt.figure(figsize=(10, 4.5)) #tamano del grafico en pixeles creo.
    plt.plot(etiquetas_tiempo, valores, marker="o", color="#1f77b4") #estetica.
    plt.title(f"Evolución de {medicion.capitalize()} - {estacion}") #tittle graphic.
    plt.xlabel("Fecha y Hora")
    plt.ylabel(medicion.capitalize())
    plt.xticks(rotation=45, ha="right") #valores del eje x a 45grados a la derecha.
    plt.grid(True, linestyle="--", alpha=0.6) #cuadriculado de fondo para mejor lectura.
    plt.tight_layout() #acomoda los margenes y centra los elementos.

    plt.savefig(ruta, dpi=300) #EXTRA: para que lo muestre en alta definicion.
    plt.close()

    return str(ruta)