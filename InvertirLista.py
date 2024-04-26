# Definir una función inversa() que calcule la inversión de una cadena.
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def longitudLista():
    lista = input("Ingrese su lista de datos separados por espacios: ").split()
    contador = 0
    for i in lista:
        contador += 1
    return contador

contador = longitudLista()
print("La longitud de la lista es:", contador)


def invertirLista(lista):
    cadena_invertida = ""
    for elemento in reversed(lista):
        cadena_invertida += elemento + " "

    return cadena_invertida.strip()

lista_palabras = input("Ingrese una cadena de palabras separadas por espacios: ").split()
cadena_invertida = invertirLista(lista_palabras)
print("La cadena invertida es:", cadena_invertida)
