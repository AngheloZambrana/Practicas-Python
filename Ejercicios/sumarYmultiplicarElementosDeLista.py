
#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números
# de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

lista = [int(x) for x in input("Ingrese su lista de datos separados por espacios: ").split()]

def sumaListas(lista):
    sumatoria = 0
    for elemento in lista:
        sumatoria += elemento
    print("La suma de los elementos de la lista es:", sumatoria)

# Función para multiplicar los elementos de una lista
def multiplicarListas(lista):
    multiplatoria = 1
    for elemento in lista:
        multiplatoria *= elemento
    print("El resultado de multiplicar todos los elementos de la lista es:", multiplatoria)

sumaListas(lista)
multiplicarListas(lista)

