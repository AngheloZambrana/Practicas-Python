def mediaLista(lista_numeros):
    media = sum(lista_numeros) / len(lista_numeros)
    return media

entrada = input("Ingresa la lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]
resultado = mediaLista(numeros)
print(f"La media de la lista es {resultado}")
