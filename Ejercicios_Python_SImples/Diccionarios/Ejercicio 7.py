def cestaProductos():
    articulos = {}
    total = 0
    continuar = True
    while continuar:
        clave = input('¿Qué producto quieres añadir? ')
        valor = int(input(clave + ': '))
        articulos[clave] = valor
        print(articulos)
        total += valor
        continuar = input('¿Quieres añadir más productos (si/no)? ').lower() == "si"

    print("\nLista de la compra:")
    for articulo, precio in articulos.items():
        print(f"{articulo}\t{precio}")
    print(f"\nTotal\t{total}")


cestaProductos()