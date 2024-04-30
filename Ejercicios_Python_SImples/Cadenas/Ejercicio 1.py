def impresion():
    nombre = input("Ingrese el nombre del usuario: ")
    numero = int(input("Ingrese la cantidad de veces que desea imprimir: "))
    for _ in range(numero):
        print(f"El nombre del usuario es {nombre}")
impresion()