def loteriaPrimitiva():
    lista = input("Ingrese los números ganadores separados por espacios: ")
    numeros_lista = lista.split()
    numeros_enteros = [int(numero) for numero in numeros_lista]
    numeros_enteros.sort()
    print("Los números ganadores ordenados de menor a mayor son:")
    for numero in numeros_enteros:
        print(numero)
loteriaPrimitiva()