def asignacionVocal():
    lista = input("Ingrese su lista de datos separados por espacios: ").split()
    vocal = str(input("Ingrese una vocal: "))
    lista.insert(0, vocal)
    print(lista)
asignacionVocal()