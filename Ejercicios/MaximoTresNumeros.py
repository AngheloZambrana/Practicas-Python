#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos
def maximoTres():
    numero1 = int(input("Ingrese su numero: "))
    numero2 = int(input("Ingrese su segundo numero: "))
    numero3 = int(input("Ingrese su tercer numero: "))
    if (numero1 > numero2) and (numero1 > numero3):
        print("El numero mayor es: " + str(numero1))
    elif (numero2 > numero1) and (numero2 > numero3):
        print("El numero mayor es: " + str(numero2))
    elif (numero3 > numero1) and (numero3 > numero2):
        print("El numero mayor es: " + str(numero3))
    else:
        print("Dos o mas numeros tienen el msmo valor")

maximoTres()