def categorias():
    listaCategorias = ["Favoritos", "Nuevos", "Estrenos", "Super Estrenos"]
    codigos = list(range(1, len(listaCategorias) + 1))
    precios = [2.50, 3.00, 3.50, 4.00]
    deudas = [0.50, 0.75, 1.00, 1.50]
    return listaCategorias, codigos, precios, deudas

def asignarDeuda(categoria, deudas):
    if categoria == "Favoritos":
        return deudas[0]
    elif categoria == "Nuevos":
        return deudas[1]
    elif categoria == "Estrenos":
        return deudas[2]
    elif categoria == "Super Estrenos":
        return deudas[3]
    else:
        print("Su categoria no se encuentra en nuestra lista")
