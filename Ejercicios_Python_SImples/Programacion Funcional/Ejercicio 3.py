def aplicarLista(funcion, lista_numero):
    lista_final = []
    for i in range(len(lista_numero)):
        resultado = funcion(lista_numero[i])
        lista_final.append(resultado)
    return lista_final

def cuadradosLista(numero):
    operacion = numero ** 2
    return operacion

entrada = input("Ingresa la lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]
resultado = aplicarLista(cuadradosLista, numeros)
print(f"La lista con funcion aplicada seria {resultado}")