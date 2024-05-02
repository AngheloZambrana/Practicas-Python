def CalculoFactorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

# Ejemplo de uso:
numero_usuario = int(input("Ingrese su número para calcular su factorial: "))
resultado = CalculoFactorial(numero_usuario)
print(f"El factorial de {numero_usuario} es {resultado}")
