#Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
#las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
#últimas tiene que decir que riman un poco y si no, que no riman.

def rimas():
    palabra1 = input("Ingrese una palabra: ").lower()
    palabra2 = input("Ingrese su otra palabra: ").lower()

    lista_palabra1 = list(palabra1)
    lista_palabra2 = list(palabra2)

    comparador1 = len(lista_palabra1) - 3
    comparador2 = len(lista_palabra1) - 2
    comparador3 = len(lista_palabra1) - 1

    Scomparador1 = len(lista_palabra2) - 3
    Scomparador2 = len(lista_palabra2) - 2
    Scomparador3 = len(lista_palabra2) - 1

    if lista_palabra1[comparador1] == lista_palabra2[Scomparador1]:
        if lista_palabra1[comparador2] == lista_palabra2[Scomparador2]:
            if lista_palabra1[comparador3] == lista_palabra2[Scomparador3]:
                print("Ambas palabras riman")
    else:
        print("Sus palabras no riman")

rimas()