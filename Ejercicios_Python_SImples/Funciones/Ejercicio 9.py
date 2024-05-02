def calcular_mcd(numero1, numero2):
    mcd = 1
    for i in range(2, min(numero1, numero2) + 1):
        if numero1 % i == 0 and numero2 % i == 0:
            mcd = i
    return mcd
def calcular_mcm(numero1, numero2):
    mcm = (numero1 * numero2) // calcular_mcd(numero1, numero2)
    return mcm

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

mcd = calcular_mcd(numero1, numero2)
print(f"El máximo común divisor de {numero1} y {numero2} es: {mcd}")

mcm = calcular_mcm(numero1, numero2)
print(f"El mínimo común múltiplo de {numero1} y {numero2} es: {mcm}")
