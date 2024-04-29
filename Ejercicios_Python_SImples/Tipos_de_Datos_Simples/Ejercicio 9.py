#Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

def capitalCalculo():
    inversion = float(input("Ingrese la cantidad que desaea invertir: "))
    interesAnual = float(input("Ingrese su interes anual: "))
    años = int(input("Ingrese el numero de años: "))
    capital = inversion * (1 + interesAnual) ** años

    print(f"La capital obtenida por la inversion es de {capital}")

capitalCalculo()