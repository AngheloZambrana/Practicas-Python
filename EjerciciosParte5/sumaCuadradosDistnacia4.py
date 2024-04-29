# Para un numero N menor de 100. Mostrar la suma de los cuadrados de los
# números que están separados entre si cuatro posiciones.
def sumaCuadrados():
    suma_cuadrados = 0
    for i in range(1, 100):
        if i + 4 < 100:
            suma_cuadrados += (i + 4) ** 2
    print("La suma de los cuadrados de los números separados por cuatro posiciones es:", suma_cuadrados)


sumaCuadrados()