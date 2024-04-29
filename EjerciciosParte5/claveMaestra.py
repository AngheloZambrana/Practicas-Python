#Los números de las claves de dos cajas fuertes están mezcladas en un
#número entero llamado clave maestra. Determine ambas claves, la primera
#clave se construye con los dígitos impares de la clave maestra y la
#segunda con los pares. Ejemplo: Clave Maestra= 12345, clave1=135,
#clave2=24.

def claveMaestra ():
    numero = [int(x) for x in str(int(input("Ingrese su clave maestra: ")))]
    pares = []
    impares = []
    longitud = len(numero)
    index = 0
    for _ in range(longitud):
        if numero[index] % 2 == 0:
            pares.append(numero[index])
        else:
            impares.append(numero[index])
        index += 1

    clave1 = int(''.join(map(str, impares)))
    clave2 = int(''.join(map(str, pares)))
    print(f"clave1: {clave1}")
    print(f"clave2: {clave2}")

claveMaestra()
