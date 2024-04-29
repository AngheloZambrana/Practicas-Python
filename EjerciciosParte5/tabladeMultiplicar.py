def tablaMultiplicar ():
    numero = int(input("Ingrese su numero: "))
    valor = 1
    for _ in range(10):
        operacion = numero * valor
        print(f"{numero} multplicador por {valor} es igual a: {operacion}")
        valor += 1

tablaMultiplicar()

