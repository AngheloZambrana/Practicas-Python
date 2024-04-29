def sumaDigitos():
    numero = [int(x) for x in str(int(input("Ingrese su numero: ")))]
    suma = sum(numero)
    print(f"La suma de los dígitos es: {suma}")

sumaDigitos()
