def cantidadDigitos():
    numero = [x for x in str(int(input("Ingrese su numero: ")))]
    contador = len(numero)
    print(f"La cantidad de digios que tiene es {contador}")

cantidadDigitos()