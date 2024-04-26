
#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def vocales():
    vocales = ["a", "e", "i", "o", "u"]
    letraUsuario = input("Ingrese su letra: ")
    if letraUsuario.lower() in vocales:
        print("Su letra es una vocal")
    else:
        print("Su letra no es una vocal")
vocales()