def invertirFrase():
    lista = input("Ingrese su lista de datos separados por espacios: ").split()
    resultado = []
    longituf = len(lista)
    index = 0
    for _ in range(longituf):
        palabra = lista[index]
        palabra_invertida = palabra[::-1]
        resultado.append(palabra_invertida)
        index += 1
    resultado.reverse()
    print(resultado)

invertirFrase()