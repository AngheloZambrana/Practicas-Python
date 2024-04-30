def cesta():
     producto_cesta = input("Por favor, ingrese los productos dentro de la cesta separados por comas: ")
     productos = producto_cesta.split(',')
     for index, producto in enumerate(productos, start=1):
        print(f"Producto {index}: {producto.strip()}")


cesta()