#Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma
# en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
#****
#*********
#*******
lista = [int(x) for x in input("Ingrese su lista de datos separados por espacios: ").split()]

def histogram(lista):
    for numero in lista:
        muestra = []
        for _ in range(numero):
            muestra.append("*")
        resultado = "".join(muestra)
        print(resultado)

histogram(lista)