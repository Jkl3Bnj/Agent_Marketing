from Calendario import generar_calendario, asignar_publicaciones_por_clase
from export import exportar_excel

def main():
    # Fechas de inicio y fin
    fecha_inicio = "2025-09-01"
    fecha_fin = "2025-11-30"
    
    # Definir redes sociales y clases
    redes_sociales = ["Instagram", "TikTok", "LinkedIn", "Facebook", "YouTube"]
    clases = ["promocional", "informativo", "comunidad"]

    # Crear el calendario
    calendario = generar_calendario(redes_sociales, clases, fecha_inicio, fecha_fin)

    # Asignar publicaciones a cada clase de cada red social
    for red_social in redes_sociales:
        for clase in clases:
            calendario[red_social][clase] = asignar_publicaciones_por_clase(
                fecha_inicio, fecha_fin, 7, red_social, clase
            )

    # Exportar el calendario a Excel
    exportar_excel(calendario)

    print("Calendario generado y exportado con éxito.")

if __name__ == "__main__":
    main()
