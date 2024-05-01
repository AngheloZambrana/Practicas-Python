def formulario():
    nombre = input("Ingrese su nombre por favor: ")
    edad = int(input("Ingrese su edad por favor: "))
    direccion = input("Ingrese su dirección donde vive: ")
    telefono = input("Ingrese su número de teléfono: ")

    diccionario = {"Nombre": nombre, "Edad": edad, "Direccion": direccion, "Telefono": telefono}

    print(f"{diccionario['Nombre']} tiene {diccionario['Edad']} años, vive en {diccionario['Direccion']} y su número de teléfono es {diccionario['Telefono']}.")

formulario()