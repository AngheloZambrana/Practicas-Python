def agregarDiccionario():
    diccionario = {}

    while True:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        carrera = input("Ingrese su carrera: ")

        diccionario["Nombre"] = nombre
        diccionario["Edad"] = edad
        diccionario["Carrera"] = carrera

        print("Contenido del diccionario:", diccionario)

        continuar = input("¿Desea agregar más información? (s/n): ")
        if continuar.lower() != 's':
            break


agregarDiccionario()