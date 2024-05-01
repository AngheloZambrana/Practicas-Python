def eliminarPosicion3():
    lista_abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']
    nueva_lista = []
    for i, letra in enumerate(lista_abecedario, start=1):
        if i % 3 != 0:
            nueva_lista.append(letra)
    print(f"Abecedario resultante {nueva_lista}")

eliminarPosicion3()

