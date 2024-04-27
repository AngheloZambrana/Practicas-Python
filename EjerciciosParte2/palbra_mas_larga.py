# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga():
    lista = input("Ingrese su lista de datos separados por espacios: ").split()

    if len(lista) > 0:
        maximo = lista[0]
        for palabra in lista:
            if len(palabra) > len(maximo):
                maximo = palabra
        print("La palabra más larga es:", maximo)
    else:
        print("La lista está vacía.")

mas_larga()
