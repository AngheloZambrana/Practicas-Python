#Definir una función superposicion() que tome dos listas y devuelva True si
# tienen al menos 1 miembro en común o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado

lista1 = [int(x) for x in input("Ingrese su lista 1 de datos separados por espacios: ").split()]
lista2 = [int(x) for x in input("Ingrese su lista 2 de datos separados por espacios: ").split()]

def elementoComun(lista1, lista2):
    for elemento in lista1:
        for elemento2 in lista2:
            if elemento == elemento2:
                return True
    return False

if elementoComun(lista1, lista2):
    print("Tienen al menos un elemento en común.")
else:
    print("No tienen elementos en común.")


