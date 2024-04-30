#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un
# cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el
# cociente y el resto de la división entera respectivamente.

def divisionEnteros():
    x = int(input("Ingrese su primer numero entero: "))
    y = int(input("Ingrese su segundo numero entero: "))
    residuo = x % y
    cociente = x // y
    print(f"La division entre {x} y {y} da un cociente {cociente} y un resto {residuo}")

divisionEnteros()