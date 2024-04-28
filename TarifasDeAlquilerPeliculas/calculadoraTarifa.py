from TarifasDeAlquilerPeliculas.categorias import categorias, asignarDeuda

def calcularDeuda():
    while True:
        listaCategorias, codigos, precios, deudas = categorias()

        opcion = int(input("Introduzca el codigo de la categoria de la pelicula: "))
        if opcion in codigos:
            dias = int(input("Introduzca el numero de dias de retraso en la devolucion: "))
            categoria = listaCategorias[opcion - 1]
            precio = precios[opcion - 1]
            deuda = asignarDeuda(categoria, deudas)
            total = deuda * dias
            print("Total a pagar:", total)
        else:
            print("Código de categoría inválido")
        opcion_salida = input("Si desea salir presion 1 o de lo contrario presione otro numero: ")
        if opcion_salida == '1':
            break

calcularDeuda()
