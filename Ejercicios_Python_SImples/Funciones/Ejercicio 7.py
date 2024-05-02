def cuadradosLista(lista_numeros):
    lista_cuadrados = []
    for i in range(len(lista_numeros)):
        cuadrado = lista_numeros[i] ** 2
        lista_cuadrados.append(cuadrado)
    return lista_cuadrados


entrada = input("Ingresa la lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]
resultado = cuadradosLista(numeros)
print(f"Los cuadrados de la lista es{resultado}")
