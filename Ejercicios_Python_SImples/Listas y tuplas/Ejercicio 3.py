def notasMaterias():
    lista = input("Ingrese su lista de datos separados por espacios: ").split()
    longitud = len(lista)
    notasFinales = []

    for materia in lista:
        nota = int(input(f"Ingrese tu nota que sacaste en {materia}: "))
        notasFinales.append(nota)

    for i in range(longitud):
        print(f"Te sacaste {notasFinales[i]} en {lista[i]}")


notasMaterias()
