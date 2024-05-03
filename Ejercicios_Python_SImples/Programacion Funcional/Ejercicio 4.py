def aplicarLista(funcion, lista_numero):
    lista_final = []
    for i in range(len(lista_numero)):
        resultado = funcion(lista_numero[i])
        if resultado:
            lista_final.append(lista_numero[i])
    return lista_final

def espar(numero):
    return numero % 2 == 0

entrada = input("Ingresa la lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]
resultado = aplicarLista(espar, numeros)
print(f"La lista con funcion aplicada seria {resultado}")