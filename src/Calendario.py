import datetime

def crear_calendario_publicaciones():
    fechas_clave = [
        {"fecha": "2023-10-01", "evento": "Lanzamiento Producto A"},
        {"fecha": "2023-10-10", "evento": "Día Internacional de la Mujer"}
    ]

    calendario = []
    for fecha in fechas_clave:
        fecha_obj = datetime.datetime.strptime(fecha["fecha"], "%Y-%m-%d")
        calendario.append(f"Publicación en {fecha_obj.strftime('%A, %B %d, %Y')}: {fecha['evento']}")

    return calendario
