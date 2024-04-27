# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
# También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

def cantidad_nombres_con_letra():
    letra = input("Ingrese la letra a buscar: ").lower()
    nombres = input("Ingrese los nombres separados por espacios: ").split()
    contador = 0
    for nombre in nombres:
        if nombre.lower().startswith(letra):
            contador += 1
    print("La cantidad de nombres que comienzan con la letra ", letra, "es: " , contador)

cantidad_nombres_con_letra()
