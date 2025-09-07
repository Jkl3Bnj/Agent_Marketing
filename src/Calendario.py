from datetime import datetime, timedelta

def generar_calendario(redes_sociales, clases, fecha_inicio, fecha_fin):
    calendario = {}
    for red_social in redes_sociales:
        calendario[red_social] = {}
        for clase in clases:
            calendario[red_social][clase] = []
    return calendario

def asignar_publicaciones_por_clase(fecha_inicio, fecha_fin, frecuencia, red_social, clase):
    publicaciones = []
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

    while fecha_inicio <= fecha_fin:
        publicaciones.append({
            "fecha": fecha_inicio.strftime('%Y-%m-%d'),
            "red_social": red_social,
            "clase": clase,
            "tema": f"Tema para {clase} en {red_social}",
            "copy": f"Texto para {clase}",
            "hashtags": "#Hashtags",
        })
        fecha_inicio += timedelta(days=frecuencia)  # Ajustar según la frecuencia

    return publicaciones
