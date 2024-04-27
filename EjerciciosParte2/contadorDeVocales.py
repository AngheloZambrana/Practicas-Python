#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras
# "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

def contadorVocales():
    palabra = input("Ingrese la palabra que usted quiera: ").lower()
    vocales = ["a", "e", "i", "o", "u"]
    contador = {vocal: 0 for vocal in vocales}
    for letra in palabra:
        if letra in vocales:
            contador[letra] += 1

    for vocal, cantidad in contador.items():
        print(f"La palabra tiene {cantidad} letra(s) '{vocal}'")
contadorVocales()