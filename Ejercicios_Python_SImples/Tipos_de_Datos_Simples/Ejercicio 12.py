# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el
# programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y
# el coste final total.

def panaderia():
    precio_habitual = 3.49
    descuento = 0.6

    barras_vendidas = int(input("Ingrese el número de barras vendidas que no son del día: "))
    precio_descuento = precio_habitual * (1 - descuento)
    coste_total = precio_descuento * barras_vendidas

    print(f"El precio habitual de una barra de pan es: {precio_habitual:.2f}€")
    print(f"El descuento que se le hace por no ser del día es del {descuento * 100:.0f}%")
    print(f"El coste final total es: {coste_total:.2f}€")

panaderia()
