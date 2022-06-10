from dominio.Pelicula import Pelicula
from Servicio.CatalogoPelicula import CatalogoPelicula

menu = None

while menu != 4:
    try:
        print('Opciones: ')
        print('1) Agregar Pelicula')
        print('2) Listar Peliculas')
        print('3) Eliminar archivo de peliculas')
        print('4) Salir')
        menu = int(input('Escribe una opción del 1-4: '))

        if menu == 1:
            nombre_pelicula = input('Proporciones el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPelicula.agregar_peliculas(pelicula)

        elif menu == 2:
            CatalogoPelicula.listar_peliculas()
        elif menu == 3:
            CatalogoPelicula.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrió un error {e}')
        menu = None


else:
    print('Salimos del menu')
