def palindromo():
    palabra = input("Ingrese la palabra que desea verificar: ")
    palbra_invertida = palabra[::-1]
    longitud = len(palabra)
    es_palindromo = True
    for i in range(longitud):
        if palabra[i] != palbra_invertida[i]:
            es_palindromo = False
            break
    if es_palindromo:
        print("Es un palindromi")
    else:
        print("No es un palíndromo")

palindromo()