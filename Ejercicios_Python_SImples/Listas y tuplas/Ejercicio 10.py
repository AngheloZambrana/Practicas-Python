def calculadoraPreios():
    precios = [50, 75, 46, 22, 80, 65, 8]
    precios.sort(reverse=False)
    print(f"Tu valor mas pequeño es {precios[0]}")
    print(f"Tu valor mas grande es {precios[len(precios) - 1]}")

calculadoraPreios()