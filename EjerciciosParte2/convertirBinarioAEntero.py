# Construir un pequeño programa que convierta números binarios en enteros.

def convertirBinarioAEntero():
    numero_binario = input("Ingrese un número binario: ")
    numero_entero = int(numero_binario, 2)
    print("El número entero equivalente es:", numero_entero)

convertirBinarioAEntero()