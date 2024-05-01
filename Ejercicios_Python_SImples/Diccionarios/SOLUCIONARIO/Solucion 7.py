def solucion():
    cesta = {}
    continuar = True
    while continuar:
        item = input('Introduce un artículo: ')
        precio = float(input('Introduce el precio de ' + item + ': '))
        cesta[item] = precio
        continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
    coste = 0
    print('Lista de la compra')
    for item, precio in cesta.items():
        print(item, '\t', precio)
        coste += precio
    print('Coste total: ', coste)
solucion()