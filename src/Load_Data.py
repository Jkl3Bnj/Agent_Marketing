import json

def cargar_guia_de_marca():
    with open('D:\VisualCode\Agent_Marketing\src\Estilo.json', 'r') as archivo:
        guia_marca = json.load(archivo)
    return guia_marca
