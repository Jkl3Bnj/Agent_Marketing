import pandas as pd
import json

def exportar_excel(calendario):
    data = []
    for red_social, clases in calendario.items():
        for clase, publicaciones in clases.items():
            for pub in publicaciones:
                data.append({
                    "Red Social": red_social,
                    "Clase": clase,
                    "Fecha": pub["fecha"],
                    "Hashtags": pub["hashtags"]
                })
    df = pd.DataFrame(data)
    df.to_excel("calendario_por_clase.xlsx", index=False)

def exportar_json(calendario):
    with open("calendario.json", "w", encoding="utf-8") as file:
        json.dump(calendario, file, indent=4, ensure_ascii=False)
