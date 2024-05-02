def calculoIVA(numero, porcentaje = 0.21):
    operacion = numero * porcentaje
    total = numero + operacion
    return total


# Ejemplo de uso:
cantidad_sin_iva = int(input("Ingrese su cantidad sin IVA: "))
cantidad_porcentaje = float(input("Ingrese el porcentaje de iva que quiere: "))
resultado = calculoIVA(cantidad_sin_iva, cantidad_porcentaje)   
print(f"El total de {cantidad_sin_iva} añadiendole el {cantidad_porcentaje}% es de {resultado}")
