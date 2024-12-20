import os
from clubbaloncesto import Jugador, Club, Entrenador, Equipo

os.system('cls')

club = Club()
opcion=club.print_menu()

print(opcion)

#jugador = Jugador()
#jugador.nuevo_jugador()
#jugador.print_persona()

entrenador = Entrenador("Paco Marti",49,185,81)

equipocadete = Equipo("cadete A","Cadete", entrenador)
equipojunior = Equipo("junior A","Junior", entrenador)

entrenador.print_persona()
entrenador.print_equipos()