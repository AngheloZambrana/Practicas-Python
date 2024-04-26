#Definir una función generar_n_caracteres() que tome un entero n y devuelva el
# caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def caracteres():
    cantidad = int(input("Ingrese su cantidad de caracteres: "))
    letra = input("Ingrese la letra que desea ingresar: ")
    lista = []
    for _ in range(cantidad):  # Iterar 'cantidad' veces
        lista.append(letra)    # Agregar la letra a la lista en cada iteración
    resultado = "".join(lista)  # Convertir la lista en una cadena
    print("El resultado es:", resultado)

caracteres()
()