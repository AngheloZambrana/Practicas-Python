def facturasUsuario():
    diccionario = {}
    total = 0
    total_total = 0
    continuar = True

    while continuar:
        print(f"Que desea realizar el usuario \n 1. Añadir Factura \n 2. Pagar Factura \n 3. Terminar")
        opcion = int(input("Ingrese una de las opciones: "))

        if opcion == 1:
            numero_factura = int(input("¿Ingrese el numero de la factura  que quieres añadir?: "))
            valor_factura = int(input(str(numero_factura) + ': '))
            diccionario[numero_factura] = valor_factura
            print(diccionario)
            total += valor_factura
            total_total += valor_factura


        elif opcion == 2:
            if diccionario:
                numero_factura = int(input("Ingrese el número de la factura que desea pagar: "))
                if numero_factura in diccionario:
                    valor_factura = diccionario.pop(numero_factura)
                    print(f"Factura {numero_factura} pagada correctamente.")
                    total -= valor_factura
                else:
                    print("La factura especificada no existe en el sistema.")
            else:
                print("No hay facturas pendientes.")

        elif opcion == 3:
            print("Cantidad cobrada hasta el momento:", total_total)
            print("Cantidad pendiente de cobro:", sum(diccionario.values()))
            print("Gracias por usar el sistema de gestión de facturas.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


facturasUsuario()