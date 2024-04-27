#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2
# (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3
# números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una
# lista de números y devuelva el mas grande.

def max_in_list():
    lista = [int(x) for x in input("Ingrese su lista de datos separados por espacios: ").split()]

    if len(lista) > 0:
        maximo = lista[0]
        for numero in lista:
            if numero > maximo:
                maximo = numero
        print("El número mayor es:", maximo)
    else:
        print("La lista está vacía.")

max_in_list()
