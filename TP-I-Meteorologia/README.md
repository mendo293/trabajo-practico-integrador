# TP Integrador 1 - Parte 1: Conversor de TXT a JSON (SMN)

## Información del Proyecto

- **Materia:** Programación I - Comisión 3 - Ingeniería Electrónica y Telecomunicaciones
- **Fecha de Primera Entrega:** 31/08/2026
- **Fecha de Segunda Entrega:** 14/09/2026
- **Docente:** 
  - Linquiman Ventura, Lautaro Yamil
- **Nombre del grupo:** 
  - Los Calamares
- **Integrantes:** 
  - Calabresi, Luciana Calabresi
  - Mendoza Ruffin, Alan Michael

---

## Descripción del Proyecto
Este programa realiza la ingesta, validación y conversión de datos meteorológicos extraídos desde archivos de texto plano del Servicio Meteorológico Nacional (SMN) hacia un formato estructurado en JSON. 

Permite depurar datos erróneos, registrar explicaciones de fallas y dejar la información limpia lista para ser utilizada.
---

## Estructura del Proyecto
```text
.
├── adaptar_datos.py   # Programa principal.
├── validaciones.py    # Programa de validaciones y parseo de datos.
├── datos/
│   ├── observaciones.txt   # Archivo de entrada .txt
│   └── observaciones.json  # Archivo resultante generado .json
└── README.md          # Descripción del proyecto
```

---

## Forma de Ejecución

El programa se ejecuta desde la terminal pasando como primer argumento la ruta del archivo `.txt` de origen y como segundo argumento la ruta de destino del archivo `.json`.

```bash
python adaptar_datos.py datos/observaciones.txt datos/observaciones.json
