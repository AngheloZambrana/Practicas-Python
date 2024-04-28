from GaleriaDeProductos.productos import productosGaleria, asignarPrecio


def generarFactura():
    productos, codigos = productosGaleria()
    precios = [25.00, 25.50, 50.50, 90.00, 90.50, 100.00, 0]

    carrito = {}

    while True:
        codigo = int(input("Introduzca el código del producto (0 para terminar): "))
        if codigo == 0:
            break

        if codigo not in codigos:
            print("Código de producto inválido. Inténtelo de nuevo.")
            continue

        cantidad = int(input("Introduzca el número de unidades: "))

        producto = productos[codigo - 1]
        precio = asignarPrecio(producto, precios)
        subtotal = precio * cantidad

        if producto in carrito:
            carrito[producto]["cantidad"] += cantidad
            carrito[producto]["subtotal"] += subtotal
        else:
            carrito[producto] = {"cantidad": cantidad, "precio_unitario": precio, "subtotal": subtotal}

    total = sum(info["subtotal"] for info in carrito.values())

    print("\nFactura:")
    for producto, info in carrito.items():
        print(f"{producto}: {info['cantidad']} x ${info['precio_unitario']:.2f} = ${info['subtotal']:.2f}")
    print(f"Total a pagar: ${total:.2f}")


generarFactura()
