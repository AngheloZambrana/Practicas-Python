#Escriba una función es_bisiesto() que determine si un año determinado es un año
#bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

def añoBisiesto():
    año = int(input("Ingrese el año que desea verificar: "))
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")

añoBisiesto()