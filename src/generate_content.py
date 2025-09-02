import datetime


def generar_contenido_y_calendario(guia_marca):
    """
    Genera contenido para cada red social y lo asocia con las fechas clave del calendario.
    """
    publicaciones = {}
    calendario_publicaciones = []

    # Generar contenido para cada red social
    for red_social, tono in guia_marca["tonos"]["plataformas"].items():
        if red_social == "Instagram":
            publicaciones[red_social] = f"Post en Instagram con tono {tono}. ¡Usa imágenes estéticas!"
        elif red_social == "TikTok":
            publicaciones[red_social] = f"Post en TikTok con tono {tono}. ¡Hazlo divertido y trendy!"
        elif red_social == "LinkedIn":
            publicaciones[red_social] = f"Post en LinkedIn con tono {tono}. ¡Hazlo profesional y educativo!"
        elif red_social == "Facebook":
            publicaciones[red_social] = f"Post en Facebook con tono {tono}. ¡Conéctate emocionalmente con los usuarios!"
        elif red_social == "Youtube":
            publicaciones[red_social] = f"Video en Youtube con tono {tono}. ¡Informa y entretén a la audiencia!"
        elif red_social == "Spotify":
            publicaciones[red_social] = f"Podcast en Spotify con tono {tono}. ¡Relaja y educa a los oyentes!"

    # Crear el calendario de publicaciones y asociarlo con las publicaciones generadas
    fechas_clave = [
        {"fecha": "2023-10-01", "evento": "Lanzamiento Producto A"},
        {"fecha": "2023-10-10", "evento": "Día Internacional de la Mujer"}
    ]

    for fecha in fechas_clave:
        fecha_obj = datetime.datetime.strptime(fecha["fecha"], "%Y-%m-%d")
        evento = fecha["evento"]
        calendario_publicaciones.append(f"{fecha_obj.strftime('%A, %B %d, %Y')} - Evento: {evento}")

        for red_social, contenido in publicaciones.items():
            calendario_publicaciones.append(f"  Publicación en {red_social}: {contenido}")

    return calendario_publicaciones
