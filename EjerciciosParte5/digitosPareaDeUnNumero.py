def digitosPares():
    numero = [int(x) for x in str(int(input("Ingrese su numero: ")))]
    pares = []
    longitud = len(numero)
    index = 0
    for _ in range(longitud):
        if numero[index] % 2 == 0:
            pares.append(numero[index])
        index += 1
    print(f"Digitos pares: {pares}")

digitosPares()

