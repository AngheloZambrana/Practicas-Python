#Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla
# la suma de todos los enteros desde 1 hasta . La suma de los primeros enteros positivos puede ser
# calculada de la siguiente forma:

def sumaN():
    n = int(input("Ingrese su numero N: "))
    suma = (n * (n + 1) / 2)
    print(f"El resultado de su operacion (n * (n + 1) / 2) es: {suma}")
sumaN()