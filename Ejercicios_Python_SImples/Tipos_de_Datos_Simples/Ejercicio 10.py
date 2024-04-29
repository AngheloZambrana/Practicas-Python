# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por
# correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso
# de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
# Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso
# total del paquete que será enviado.

def jugueteria():
    num_payasos = int(input("Ingrese el numero de payasos vendidos: "))
    num_muñecas = int(input("Ingrese el numero de muñecas vendidos: "))
    payaso = 112
    muñeca = 75

    pesoTotal = (payaso * num_payasos) + (muñeca * num_muñecas)
    print(f"Si se vendieron {num_payasos} payasos y {num_muñecas} muñecas:")
    print(f"El peso total del paquete será de {pesoTotal} gramos.")
jugueteria()