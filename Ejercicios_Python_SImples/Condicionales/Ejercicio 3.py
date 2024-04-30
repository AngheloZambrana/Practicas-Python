def divisiones():
    numero = int(input("Ingrese el numero que desea dividir: "))
    divisor = int(input("Ingrese el divisor: "))
    if divisor == 0:
        print("Error el divisor no puede ser cero")
    else:
        division = numero / divisor
        print(f"El resultado es {division}")
divisiones()