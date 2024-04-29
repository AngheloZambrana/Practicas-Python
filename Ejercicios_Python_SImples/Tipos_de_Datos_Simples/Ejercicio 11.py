## Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance
# final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada
# en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
# la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

def cuentaAhorros():
    interesAnual = 0.04
    dineroDepositado = float(input("Ingrese la cantidad de dinero depositado: "))

    primerAño = dineroDepositado * (1 + interesAnual)
    segundoAño = primerAño * (1 + interesAnual)
    tercerAño = segundoAño * (1 + interesAnual)

    print(f"En el primer año la cantidad es de {primerAño:.2f}")
    print(f"En el segundo año la cantidad es de {segundoAño:.2f}")
    print(f"En el tercer año la cantidad es de {tercerAño:.2f}")

cuentaAhorros()