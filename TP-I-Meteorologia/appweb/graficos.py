#3
from pathlib import Path
import matplotlib.pyplot as plt 


def generar_grafica(filtrados, estacion, medicion, ruta_salida): 
    if not filtrados:
        return "" 

    ruta = Path(ruta_salida) 
    ruta.parent.mkdir(parents=True, exist_ok=True) 
    
    etiquetas_tiempo = []
    valores = []

    for reg in filtrados:
        fecha = reg.get("fecha", "")
        hora = reg.get("hora", "")
        etiquetas_tiempo.append(f"{fecha} {hora}h")
        valores.append(reg[medicion])

    plt.figure(figsize=(10, 4.5)) 
    plt.plot(etiquetas_tiempo, valores, marker="o", color="#1f77b4") 
    plt.title(f"Evolución de {medicion.capitalize()} - {estacion}") 
    plt.xlabel("Fecha y Hora")
    plt.ylabel(medicion.capitalize())
    plt.xticks(rotation=45, ha="right") 
    plt.grid(True, linestyle="--", alpha=0.6) 
    plt.tight_layout() 

    plt.savefig(ruta, dpi=300) 
    plt.close()

    return str(ruta)