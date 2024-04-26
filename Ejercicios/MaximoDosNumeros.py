#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
# (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
def maximo():
    num1 = int(input("Ingrese su numero: "))
    num2 = int(input("Ingrese su segundo numero: "))
    if num1 > num2:
        print("El numero mayor es: " + str(num1))
    else:
        print("El numero mayor es: " + str(num2))

maximo()