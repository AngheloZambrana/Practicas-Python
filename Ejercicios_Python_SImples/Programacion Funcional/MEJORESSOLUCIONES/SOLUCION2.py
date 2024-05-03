import math


def seno(angulo):
    angulo_radianes = math.radians(angulo)
    operacion = math.sin(angulo_radianes)
    return operacion


def coseno(angulo):
    angulo_radianes = math.radians(angulo)
    operacion = math.cos(angulo_radianes)
    return operacion


def tangente(angulo):
    angulo_radianes = math.radians(angulo)
    operacion = math.tan(angulo_radianes)
    return operacion


def exponencial(numero):
    exponencial = math.exp(numero)
    return exponencial


def logaritmo_neperiano(numero):
    logaritmo_neperiano = math.log(numero)
    return logaritmo_neperiano


def calcular_funcion(funcion, valor):
    resultados = []
    for i in range(1, valor + 1):
        resultados.append(funcion(i))
    return resultados


while True:
    print(
        "1. Sacar Seno\n2. Sacar Coseno\n3. Sacar Tangente\n4. Sacar Exponencial\n5. Sacar Logaritmo Neperiano\n6. Salir")
    opcion = int(input("Ingrese la opción del menú que desea realizar: "))
    if opcion == 6:
        print("¡Gracias por usar la calculadora!")
        break
    valor = int(input("Ingrese el valor hasta el cual desea calcular la función: "))
    if opcion == 1:
        resultados = calcular_funcion(seno, valor)
        print("Tabla de seno:")
    elif opcion == 2:
        resultados = calcular_funcion(coseno, valor)
        print("Tabla de coseno:")
    elif opcion == 3:
        resultados = calcular_funcion(tangente, valor)
        print("Tabla de tangente:")
    elif opcion == 4:
        resultados = calcular_funcion(exponencial, valor)
        print("Tabla de exponencial:")
    elif opcion == 5:
        resultados = calcular_funcion(logaritmo_neperiano, valor)
        print("Tabla de logaritmo neperiano:")
    else:
        print("Opción inválida, por favor seleccione una opción válida.")
        continue

    for i, resultado in enumerate(resultados, start=1):
        print(f"{i}: {resultado}")
