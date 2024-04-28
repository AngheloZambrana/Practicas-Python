#Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a $100.00,
# el programa dirá que el cliente no aplica a la promoción. Pero si la persona ingresa una cantidad en compras igual o
# superior a $100.00, el programa genera de forma aleatoria un número entero del cero al cinco. Cada número
# corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente
# recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro
# colores, sí se aplicará un descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre
# el total de compra que introdujo inicialmente el usuario, de manera que el programa mostrará un nuevo valor a pagar
# luego de haber aplicado el descuento.

import random
import time
def descuentosColor():
    try:
        cantidadInicial = float(input("Introduzca la cantidad total de la compra(2.50): "))
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido.")
        return

    if cantidadInicial >= 100.00:
        print("Su gasto es mayor a $100.00 aplica a la promocion")
        print("Ahora saque una bola para verificar su promocion")
        time.sleep(2)
        print("Y la bola que saco es .....")
        time.sleep(2)
        color = random.randint(1,5)
        if color == 1:
            print("La bola que saco es blanco no obtiene ninguna promocion")
            print(f"Su total a pagar es {cantidadInicial}")
        elif color == 2:
            print("La bola que saco es roja obtiene 10%")
            resultado = cantidadInicial * 0.1
            print(f"Felcidades su total a pagar es {resultado}")
        elif color == 3:
            print("La bola que saco es azul obtiene 20%")
            resultado = cantidadInicial * 0.2
            print(f"Felcidades su total a pagar es {resultado}")
        elif color == 4:
            print("La bola que saco es verde obtiene 25%")
            resultado = cantidadInicial * 0.25
            print(f"Felcidades su total a pagar es {resultado}")
        elif color == 5:
            print("La bola que saco es amarilla obtiene 50%")
            resultado = cantidadInicial * 0.5
            print(f"Felcidades su total a pagar es {resultado}")
    else:
        print("Su gasto es menor a 100.00 no aplica a la promocion")

descuentosColor()