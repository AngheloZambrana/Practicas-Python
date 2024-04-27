#Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

def tuplaEdades():
    edades_str = input("Ingrese las edades separadas por espacios: ")
    edades = [int(edad) for edad in edades_str.split()]
    contador = 0
    for edad in edades:
        if edad > 20:
            contador += 1
    print("La cantidad de personas con edades superiores a 20 es:", contador)

tuplaEdades()
