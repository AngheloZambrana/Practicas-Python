import math

def ValoresAtipicos(lista_numeros):
    valores_atipicos = []
    media = sum(lista_numeros) / len(lista_numeros)
    varianza = sum((x - media) ** 2 for x in lista_numeros) / len(lista_numeros)
    desviacion_tipica = math.sqrt(varianza)
    for i in range(len(lista_numeros)):
        puntuacion_tipica = (lista_numeros[i] - media) / desviacion_tipica
        if puntuacion_tipica > 3 or puntuacion_tipica < -3:
            valores_atipicos.append(lista_numeros[i])
    return valores_atipicos


entrada = input("Ingresa la lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]
resultado = ValoresAtipicos(numeros)
print(f"Los valores atipicos de su lista son: {resultado}")