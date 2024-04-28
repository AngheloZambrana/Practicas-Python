#Escribe un programa que te permita jugar a una versión simplificada del
#juego Master Mind. El juego consistirá en adivinar una cadena de números
# distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2
#a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
#cadena de números. En cada intento, el programa informará de cuántos números
#han sido acertados (el programa considerará que se ha acertado un número si
#coincide el valor y la posición).

import random


def masterMind():
    longitud = int(input("Dime la longitud de la cadena: "))
    lista = []
    if longitud < 2 or longitud > 9:
        print("La longitud debe estar entre 2 y 9.")
        return
    for _ in range(longitud):
        lista.append(random.randint(0, 9))
    intentos = 0
    while True:
        numeroUsuario = input("Intenta adivinar la cadena: ")
        if len(numeroUsuario) != longitud:
            print(f"La longitud del intento debe ser {longitud}.")
            continue
        intento = [int(digito) for digito in numeroUsuario]
        aciertos = sum(1 for i in range(longitud) if intento[i] == lista[i])
        print(f"Con {numeroUsuario} has adivinado {aciertos} valores.")
        if aciertos == longitud:
            print("¡Felicidades!")
            break
        intentos += 1


masterMind()
