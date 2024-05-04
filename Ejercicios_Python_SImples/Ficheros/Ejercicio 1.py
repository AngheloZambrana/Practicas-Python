import os

def tablaMultiplicar(num):
    resultados = []
    for i in range(10 + 1):
        operacion = i * num
        resultados.append(f"{num} * {i} = {operacion}")
    return resultados

numero_ingresado = int(input("Ingrese un numero entero entre (1 y 10): "))
numero_linea_ingresado = int(input("Ingrese un numero entre(1 y 10): "))
if numero_ingresado >= 1 and numero_ingresado <= 10:
    resultados = tablaMultiplicar(numero_ingresado)
    for resultado in resultados:
        print(resultado)
else:
    print("Valor invalido")

directorio = "Utils"

if not os.path.exists(directorio):
    os.makedirs(directorio)

ruta_archivo = os.path.join(directorio, "tabla-n.txt")

def imprimirLinea(archivo, numero_linea):

    with open(ruta_archivo, 'a') as archivo:
        lineas = archivo.readlines()
        if 0 < numero_linea <= len(lineas):
            # Imprimir la línea deseada
            print(lineas[numero_linea - 1])
        else:
            print("Número de línea inválido")

imprimirLinea(ruta_archivo, numero_linea_ingresado)
