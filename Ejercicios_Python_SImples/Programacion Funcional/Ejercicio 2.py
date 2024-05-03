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

def Logaritmoneperiano(numero):
    logaritmo_neperiano = math.log(numero)
    return logaritmo_neperiano


while True:
    print("1. Sacar Seno \n2. Sacar coseno \n3. Sacar tangente \n4. Sacar exponensial \n5. Sacar Logaritmo neperiano \n Aprete cualquier numero para salir")
    opcion = int(input("Ingrese la opcion del menu que desea realizar"))
    if opcion == 1:
        angulo = int(input("Ingrese el angulo que desee calcular en (ª): "))
        resultado = seno(angulo)
        print(f"El seno de ese angulo seria {resultado}")
    elif opcion == 2:
        angulo = int(input("Ingrese el angulo que desee calcular en (ª): "))
        resultado = coseno(angulo)
        print(f"El coseno de ese angulo seria {resultado}")
    elif opcion == 3:
        angulo = int(input("Ingrese el angulo que desee calcular en (ª): "))
        resultado = tangente(angulo)
        print(f"El coseno de ese angulo seria {resultado}")
    elif opcion == 4:
        numero = int(input("Ingrese el numero: "))
        resultado = exponencial(numero)
        print(f"El coseno de ese angulo seria {resultado}")
    elif opcion == 5:
        numero = int(input("Ingrese el numero: "))
        resultado = Logaritmoneperiano(numero)
        print(f"El coseno de ese angulo seria {resultado}")
    else:
        print("GRACIAS POR USAR LA BESTO CALCULADORA")
        break