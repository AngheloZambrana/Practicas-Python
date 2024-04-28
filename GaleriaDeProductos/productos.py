def productosGaleria():
    productos = ["Camisa", "Cinturon", "Zapatos", "Pantalon", "Calcetines", "Faldas", "Gorras", "Sueter", "Corbata", "Chaqueta"]
    codigos = list(range(1, len(productos) + 1))
    return productos, codigos

def asignarPrecio(producto, precios):
    if producto == "Calcetines":
        return precios[0]
    elif producto in ["Gorras", "Cinturon", "Corbata"]:
        return precios[1]
    elif producto == "Faldas":
        return precios[2]
    elif producto in ["Camisa", "Chaqueta"]:
        return precios[3]
    elif producto == "Pantalon":
        return precios[4]
    elif producto == "Sueter":
        return precios[5]
    else:
        return precios[7]

