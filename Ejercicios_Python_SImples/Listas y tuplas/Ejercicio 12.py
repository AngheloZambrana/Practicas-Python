def multiplicacionMatrices():
    fila_a1 = [1, 2, 3]
    fila_a2 = [4, 5, 6]
    fila_b1 = [-1, 0]
    fila_b2 = [0, 1]
    fila_b3 = [1, 1]

    resultado1 = []
    resultado2 = []
    operacion1 = fila_a1[0] * fila_b1[0] + fila_a1[1] * fila_b2[1] + fila_a1[2] * fila_b3[0]
    resultado1.append(operacion1)
    operacion2 = fila_a1[0] * fila_b1[1] + fila_a1[1] * fila_b2[0] + fila_a1[2] * fila_b3[1]
    resultado1.append(operacion2)
    operacion3 = fila_a2[0] * fila_b1[0] + fila_a2[1] * fila_b2[1] + fila_a2[2] * fila_b3[0]
    resultado2.append(operacion3)
    operacion4 = fila_a2[0] * fila_b1[1] + fila_a2[1] * fila_b2[0] + fila_a2[2] * fila_b3[1]
    resultado2.append(operacion4)

    print("Resultado de la multiplicación de matrices:")
    print(resultado1)
    print(resultado2)

multiplicacionMatrices()
