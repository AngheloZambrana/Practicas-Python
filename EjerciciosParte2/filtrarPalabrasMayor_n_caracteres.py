#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
#y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras():
    lista = input("Ingrese su lista de datos separados por espacios: ").split()
    n = int(input("Ingrese la cantidad mínima de letras: "))
    palabras_filtradas = []

    for palabra in lista:
        if len(palabra) > n:
            palabras_filtradas.append(palabra)

    if palabras_filtradas:
        print("Palabras con más de", n, "caracteres:", palabras_filtradas)
    else:
        print("No hay palabras con más de", n, "caracteres en la lista.")

filtrar_palabras()
