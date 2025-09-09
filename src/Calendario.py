from datetime import datetime, timedelta
from tkinter import messagebox
from cargar_datos import cargar_guia_de_marca
from itertools import count
import json

cargar_guia_de_marca()
calendario = {}

def generar_calendario(redes_sociales, clases, fecha_inicio, fecha_fin, frecuencia, guia_marca):
    if fecha_inicio > fecha_fin:
        raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin.")
    # Iterar sobre las redes sociales
    for red_social in redes_sociales:
        calendario[red_social] = {}

        # Inicializar las clases con listas vacías
        for clase in clases:
            calendario[red_social][clase] = []

        # Verificar que hay datos configurados para la red social
        tono = guia_marca["tonos"].get(red_social, None)
        palabras_clave = guia_marca["palabras_clave"].get(red_social, None)
        llamada_accion = guia_marca["llamadas_a_la_accion"].get(red_social, None)

        # Si no tiene datos configurados, saltar a la siguiente red social
        if not tono or not palabras_clave or not llamada_accion:
            messagebox.showinfo(f"Advertencia: La red social {red_social} tiene datos incompletos en estilo.json.")
            continue  # Pasar a la siguiente red social
        # Determinar la clase basada en el tono de la red social
        if tono == "informal":
            clase_red = "informal"
        elif tono == "intermedio":
            clase_red = "intermedio"
        elif tono == "profesional":
            clase_red = "profesional"
        else:
            clase_red = "informal"  # Asignar una clase predeterminada si el tono no se encuentra

        # Generar publicaciones para la clase correspondiente
        while fecha_inicio <= fecha_fin:
            tema = f"Post para {red_social} sobre {clase_red}"
            copy = f"{tono.capitalize()} contenido sobre {clase_red}. {' '.join(palabras_clave)} {llamada_accion}"

            # Almacenar la publicación
            calendario[red_social][clase_red].append({
                "fecha": fecha_inicio.strftime('%d-%m-%Y'),
                "red_social": red_social,
                "clase": clase_red,
                "tema": tema,
                "copy": copy,
                "hashtags": "#Hashtags"
            })

            # Avanzar la fecha según la frecuencia
            fecha_inicio += timedelta(days=frecuencia)
    return calendario
