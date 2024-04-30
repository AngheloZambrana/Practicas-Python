def producto():
    nombre = input("Ingrese el nombre de su proudcto; ")
    precio = float(input("Ingrese el precio de su producto: "))
    unidades = int(input("Ingrese el numero de unidades del proudcto: "))

    costeTotal = unidades * precio

    print(f"El nombre de su producto es {nombre}")
    print(f"El precio de su producto es {precio:0>6.2f}")
    print(f"El numero de unidades es {unidades:03d}")
    print(f"El precio total seria {costeTotal:0>8.2f}")
producto()