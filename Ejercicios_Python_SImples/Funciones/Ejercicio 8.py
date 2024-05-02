import math

def cuadradosLista(lista_numeros):
    media = sum(lista_numeros) / len(lista_numeros)
    varianza = sum((x - media) ** 2 for x in lista_numeros) / len(lista_numeros)
    desviacion_tipica = math.sqrt(varianza)

    diccionario = {"Media": media, "Varianza": varianza, "Desviacion Tipica": desviacion_tipica}
    return diccionario

entrada = input("Ingresa la lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]
resultado = cuadradosLista(numeros)
print(f"El diccionario final seria{resultado}")
