# Asignatura: Fundamentos de programación
# ACTIVIDAD 1: INTRODUCCIÓN A PYTHON
# Fecha: 08.12.2024
# Autor: Mónica Penacho Collado
# Proyecto: estadisticas_jugadores
# Descripción proyecto: Aplicación realizada con Python para gestionar las estadísticas de los jugadores de un equipo de baloncesto en un partido.

# Colecciones: Listas

# Lista para almacenar los datos de los jugadores
lista_jugadores = []  # Cada jugador será una lista y almacenará las siguientes características [nombre, dorsal, canastas_3, canastas_2, canastas_1, total_puntos]

# Lista para almacenar estadísticas del equipo
# Índices: [total_puntos, total_canastas_3, total_canastas_2, total_canastas_1]
lista_estadisticas = [0, 0, 0, 0]  # Las estadísticas del equipo mostrarán tanto la puntuación total como cada una de las canastas de 3, 2 y 1

#Interfaz de usuario
'''
Muestra el menu principal de la aplicación
'''
print("--- Menu: Gestión Estadísticas de Jugadores de Baloncesto ---")
print("Seleccionar una opción: ")
print("[1] Introducir un nuevo jugador")
print("[2] Listar jugadores")
print("[3] Máximo anotador")
print("[4] Estadísticas del equipo")
print("---------------------------------")
print("[0] Salir del programa")

#Funciones

def actualizar_lista_estadisticas(jugador):
    '''
    Función que actualiza las estadísticas globales del equipo.
    '''
    lista_estadisticas[0] += jugador[5]  # Actualizar total_puntos
    lista_estadisticas[1] += jugador[2]  # Actualizar total_canastas_3
    lista_estadisticas[2] += jugador[3]  # Actualizar total_canastas_2
    lista_estadisticas[3] += jugador[4]  # Actualizar total_canastas_1

def introducir_jugador():
    '''
    Función que permite registrar un nuevo jugador: nombre, dorsal y anotaciones (canastas de 3, 2 y 1 punto y total puntos).
    '''
    # Solicitar información
    print("--- Introducir Nuevo Jugador ---")
    nombre = input("Nombre del jugador: ")
    dorsal = input("Dorsal del jugador: ")
    canastas_3 = int(input("Canastas de 3 puntos: "))
    canastas_2 = int(input("Canastas de 2 puntos: "))
    canastas_1 = int(input("Canastas de 1 punto: "))
    total_puntos = canastas_3 * 3 + canastas_2 * 2 + canastas_1
    # Crear una lista para el jugador
    jugador = [nombre, dorsal, canastas_3, canastas_2, canastas_1, total_puntos]
    # Añadir el jugador a la lista de jugadores
    lista_jugadores.append(jugador)
    # Actualizar las estadísticas globales del equipo
    actualizar_lista_estadisticas(jugador)
    print(f"Jugador {nombre} añadido correctamente.")

def listar_jugadores():
    """
    Función que muestra un listado de todos los jugadores con su dorsal y puntos totales. Se ha puesto en primer lugar el dorsal.
    """
    print("--- Listado de Jugadores ---")
    if not lista_jugadores:
        print("No hay jugadores registrados.")
    else:
        for jugador in lista_jugadores:
            print(f"Dorsal: {jugador[1]} | Nombre: {jugador[0]} | Total Puntos: {jugador[5]}")

def maximo_anotador():
    """
    Identifica y muestra al jugador con la mayor cantidad de puntos anotados.
    """
    print("--- Máximo Anotador ---")
    if not lista_jugadores:  # Comprobar si la lista está vacía
        print("No hay jugadores registrados.")
    else:
        maxima_anotacion = 0
        nombre_jugador_maxima_anotacion = ""

        # Recorrer la lista de jugadores
        for jugador in lista_jugadores:
            anotacion = jugador[5]  # Total de puntos del jugador
            if anotacion > maxima_anotacion:
                maxima_anotacion = anotacion
                nombre_jugador_maxima_anotacion = jugador[0]  # Nombre del jugador

        print(f"Máximo anotador: {nombre_jugador_maxima_anotacion} con {maxima_anotacion} puntos.")


def estadisticas_equipo_global():
    """
    Función que muestra las estadísticas globales del equipo.
    """
    print("--- Estadísticas del Equipo ---")
    if not lista_jugadores:
        print("No hay jugadores registrados.")
    else:
        print(f"Total puntos: {lista_estadisticas[0]}")
        print(f"Total canastas de 3 puntos: {lista_estadisticas[1]}")
        print(f"Total canastas de 2 puntos: {lista_estadisticas[2]}")
        print(f"Total canastas de 1 punto: {lista_estadisticas[3]}")

# Ciclo principal del programa
while True:
    # pedir opcion
    opcion = input("Introduce opción [1,2,3,4,0]: ")

    if opcion in ("0","1","2","3","4"):
        #Operaciones
        if opcion == "0":
            print("Saliendo del programa...")
            break
        elif opcion == "1":
            introducir_jugador()
        elif opcion == "2":
            listar_jugadores()
        elif opcion == "3":
            maximo_anotador()
        elif opcion == "4":
            estadisticas_equipo_global()
    else:
        print("Opción inválida. Introduce una opción válida.")

#FIN Bucle
print("Gracias por usar mi app")