def sumaDigitos():
    numero = [int(x) for x in str(int(input("Ingrese su numero: ")))]
    suma = sum(numero)
    print(f"La suma de los dígitos es: {suma}")
    if suma % 2 == 0:
        print("La suma de los digitos es par")
    else:
        print("La suma es impar")

sumaDigitos()
