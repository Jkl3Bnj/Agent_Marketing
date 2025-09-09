import pandas as pd
import json

# Función para exportar el calendario a Excel
def exportar_excel(calendario):
    data = []
    for red_social, clases in calendario.items():
        for clase, publicaciones in clases.items():
            for pub in publicaciones:
                data.append({
                    "Fecha": pub["fecha"],
                    "Red Social": pub["red_social"],
                    "Clase": pub["clase"],
                    "Tema": pub["tema"],
                    "Copy": pub["copy"],
                    "Hashtags": pub["hashtags"]
                })
    df = pd.DataFrame(data)
    df.to_excel("calendario_por_clase.xlsx", index=False)  # Guardar en un archivo Excel

# Función para exportar el calendario a JSON
def exportar_json(calendario):
    with open("calendario.json", "w", encoding="utf-8") as file:
        json.dump(calendario, file, indent=4, ensure_ascii=False)
