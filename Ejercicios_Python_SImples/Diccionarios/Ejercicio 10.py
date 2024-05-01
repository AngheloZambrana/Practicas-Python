def baseDatosClientes():
    clientes = {}
    jefe = {"Nombre": "Anghelo","Direccion": "Sacaba", "Telefono" : 74365698 ,  "Correo" : "anghelekzq@gmail.com" , "Preferente": True}
    NIF = 1
    if jefe["Preferente"] == True:
        while True:
            print("Que desea realizar el usuario:")
            print("1. Añadir Cliente")
            print("2. Eliminar Cliente")
            print("3. Mostrar Cliente")
            print("4. Listar todos los clientes")
            opcion = int(input("Ingrese una de las opciones: "))

            if opcion == 1:
                nombre = input("Ingrese el nombre del cliente que quieres añadir: ")
                direccion = input("Ingrese la dirección del cliente que quieres añadir: ")
                telefono = int(input("Ingrese el número de teléfono del cliente que quieres añadir: "))
                correo = input("Ingrese el correo del cliente que quieres añadir: ")
                preferente = bool(input("Ingrese el rango del cliente (True si es preferente, False si no): "))

                clientes[NIF] = (nombre, direccion, telefono, correo, preferente)
                print("Cliente añadido correctamente.")
                NIF += 1


            elif opcion == 2:
                if clientes:
                    nif_cliente = int(input("Ingrese el NIF del cliente que desea eliminar: "))
                    if nif_cliente in clientes:
                        del clientes[nif_cliente]
                        print("Cliente eliminado correctamente.")
                    else:
                        print("El NIF especificado no existe en el sistema.")
                else:
                    print("No hay clientes registrados.")

            elif opcion == 3:
                nif_cliente = int(input("Ingrese el NIF del cliente que desea mostrar: "))
                if nif_cliente in clientes:
                    datos_cliente = clientes[nif_cliente]
                    print("Datos del cliente:")
                    print("NIF:", nif_cliente)
                    print("Nombre:", datos_cliente[0])
                    print("Dirección:", datos_cliente[1])
                    print("Teléfono:", datos_cliente[2])
                    print("Correo:", datos_cliente[3])
                    print("Preferente:", datos_cliente[4])
            elif opcion == 4:
                print("Listado de clientes:")
                for nif, datos_cliente in clientes.items():
                    print("NIF:", nif)
                    print("Nombre:", datos_cliente[0])
                    print("Dirección:", datos_cliente[1])
                    print("Teléfono:", datos_cliente[2])
                    print("Correo:", datos_cliente[3])
                    print("Preferente:", datos_cliente[4])

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

baseDatosClientes()

