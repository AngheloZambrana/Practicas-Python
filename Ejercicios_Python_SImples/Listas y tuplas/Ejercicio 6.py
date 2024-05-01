def repetirMateria():
    lista = input("Ingrese su lista de datos separados por espacios: ").split()
    longitud = len(lista)
    notasFinales = []

    for materia in lista:
        nota = int(input(f"Ingrese tu nota que sacaste en {materia}: "))
        notasFinales.append(nota)


    for i in range(longitud):
        if notasFinales[i] < 51:
            print(f"Reprobaste {lista[i]} sacaste {notasFinales[i]}")


repetirMateria()