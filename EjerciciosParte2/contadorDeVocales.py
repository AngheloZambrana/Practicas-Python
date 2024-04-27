#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras
# "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

def contadorVocales():
    palbra = input("Ingrese la palabra que usted queira: ")
    vocales = ["a", "e", "i", "o", "u"]
    conjunto_palabra = set(palbra.lower())
    contador = {vocal: 0 for vocal in vocales}
    for letra in conjunto_palabra:
        if letra in vocales:
            contador[letra] += 1

    for vocal, cantidad in contador.items():
        print("La palabra", cantidad, "letras(s)", vocal)
contadorVocales()