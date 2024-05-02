import math
def areaCirculo(numero):
    operacion = numero * math.pi
    return operacion

def volumenCilindro(altura):
    operacion = altura * areaCirculo(radio)
    return operacion
# Ejemplo de uso:
radio = int(input("Ingrese su radio de su circulo: "))
altura = int(input("Ingrese la altura de su cilindro: "))
resultado_area = areaCirculo(radio)
resultado_volumen = volumenCilindro(altura)
print(f"Si tu area es {resultado_area} tu volumen seria {resultado_volumen}")
