from pathlib import Path
import matplotlib.pyplot as plt

def generar_grafica(filtrados, estacion, medicion, ruta_salida):
    if not filtrados:
        raise ValueError("No hay datos suficientes para generar la gráfica.")

    ruta = Path(ruta_salida)
    ruta.parent.mkdir(parents=True, exist_ok=True)

    etiquetas_tiempo = [f"{reg['fecha']} {reg['hora']}h" for reg in filtrados]
    valores = [reg[medicion] for reg in filtrados]

    plt.figure(figsize=(10, 5))
    plt.plot(
        etiquetas_tiempo,
        valores,
        label=medicion.capitalize(),
    )

    plt.title(f"Evolución de {medicion.capitalize()} - {estacion}")
    plt.xlabel("Fecha y Hora")
    plt.ylabel(medicion.capitalize())
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()

    plt.savefig(ruta)
    plt.close()

    return str(ruta)