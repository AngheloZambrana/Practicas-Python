#Diseñar un sistema de puntos para el juego El reino del dragón:
# Dejo el enlace por si alguien no lo vio. (Clase /home/fundacion/PycharmProjects/Repositorio/JuegoDelDragon/Utils/JuegoDelDragon.py)
#La idea es la siguiente: mientras el jugador vaya ganando, ira acumulando puntos.
#Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 100 puntos, entra en la segunda cueva y gana el tesoro, se le acreditan otros 100 puntos. Si el jugador pierde, saldrá en pantalla el total de los puntos que realizo y la opción de empezar de nuevo.
import time
import random

from JuegoDelDragon.Utils.JuegoDelDragon import introduccion, CambiarCueva, cheqcueva

def contadorPuntos():
    puntos = 0
    EmpezarNuevo = "si"

    while EmpezarNuevo.lower() in ["si", "sí"]:
        introduccion()
        NumCaverna = CambiarCueva()
        puntos_ganados = cheqcueva(NumCaverna)
        puntos += puntos_ganados
        print(f"Has ganado {puntos_ganados} puntos.")
        print(f"Total de puntos acumulados: {puntos}")
        print("¿Quieres jugar de nuevo? (si o no)")
        EmpezarNuevo = input()

def cheqcueva(cueva_elegida):
    print("Te acercas a la cueva...")
    time.sleep(2)
    print("Está oscuro y tenebroso...")
    time.sleep(2)
    print("Un gran dragón salta delante tuyo, abre su boca y...")
    print("")
    time.sleep(2)

    FriendlyCueva = random.randint(1, 2)

    if cueva_elegida == str(FriendlyCueva):
        print("¡Te entrega el tesoro!")
        return 100  # Ganaste 100 puntos
    else:
        print("¡El dragón te come de un bocado!")
        return 0  # No ganaste puntos

contadorPuntos()
