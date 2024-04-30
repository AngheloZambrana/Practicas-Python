# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por
# pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de
# masa corporal calculado redondeado con dos decimales.

def calcularimc():
    peso = float(input("Ingrese su peso en (kg): "))
    estatura = float(input("Ingrese su altura en (m): "))
    imc = peso / (estatura) ** 2
    print(f"Tu indice de masa corporal es {imc}")
calcularimc()