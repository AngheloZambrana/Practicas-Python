def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    binario = ''
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero //= 2
    return binario

def binario_a_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        bit = int(binario[len(binario) - 1 - i])
        decimal += bit * (2 ** i)
    return decimal

# Ejemplo de uso
numero_decimal = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero_decimal)
print(f"El número binario equivalente es: {binario}")

numero_binario = input("Ingrese un número binario: ")
decimal = binario_a_decimal(numero_binario)
print(f"El número decimal equivalente es: {decimal}")
