import math

def vector2Dimentsiones(num, num2):
    operacion = math.sqrt((num ** 2) + (num2 ** 2))
    return operacion

def vector3Dimensiones(num, num2, num3):
    operacion = math.sqrt((num ** 2) + (num2 ** 2) + (num3 ** 2))
    return operacion

opcion = int(input("Ingrese el numero de dimentsiones entre 2 y 3 para sus vectores: "))
if opcion == 1:
    x = int(input("Ingrese su valor"))
    print(f"Graciosito? Es {x}")
if opcion == 2:
    x = int(input("Ingrese el primer valor de su vector: "))
    y = int(input("Ingrese el segundo valor de su vector: "))
    resultado = vector2Dimentsiones(x, y)
    print(f"El modulo de su vector de 2 dimensiones es de: {resultado} ")

elif opcion == 3:
    x = int(input("Ingrese el primer valor de su vector: "))
    y = int(input("Ingrese el segundo valor de su vector: "))
    z = int(input("Ingrese el tercer valor de su vector: "))
    resultado = vector3Dimensiones(x, y, z)
    print(f"El modulo de su vector de 3 dimensiones es de: {resultado} ")

else:
    print("Opción no válida. Por favor, ingrese 2 o 3 para el número de dimensiones.")