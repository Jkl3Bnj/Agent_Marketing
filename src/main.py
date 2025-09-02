from Load_Data import cargar_guia_de_marca
from generate_content import generar_contenido_y_calendario

def main():
    # Cargar los datos de la guía de marca
    guia_marca = cargar_guia_de_marca()

    # Generar contenido para cada red social y crear el calendario
    calendario_publicaciones = generar_contenido_y_calendario(guia_marca)

    # Mostrar las publicaciones y el calendario
    print("Calendario de Publicaciones con contenido:")
    for publicacion in calendario_publicaciones:
        print(publicacion)

if __name__ == "__main__":
    main()
