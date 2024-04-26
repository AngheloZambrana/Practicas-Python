#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que
# tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo
# ("radar") tendría que devolver True.

from InvertirLista import inversa

def inversa(cadena):
    return cadena[::-1]

def es_palindromo(palabra):
    palabra_invertida = inversa(palabra)
    return palabra == palabra_invertida

palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")