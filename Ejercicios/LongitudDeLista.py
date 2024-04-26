# 3 - Definir una función que calcule la longitud de una lista o una cadena dada.
# (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros
# mismos resulta un muy buen ejercicio.

def longitudLista():
    lista = input("Ingrese su lista de datos separados por espacios: ").split()
    contador = 0
    for i in lista:
        contador += 1
    return contador

contador = longitudLista()
print("La longitud de la lista es:", contador)


