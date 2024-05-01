def productoEscalar():
    vector1 = [1, 2, 3, 5]
    vector2 = [-1, 0, 2, -2]
    multiplicacion = []

    if len(vector1) == len(vector2):
        for i in range(len(vector1)):
            operacion = vector1[i] * vector2[i]
            multiplicacion.append(operacion)
    else:
        print("No se puede realizar el producto escalar, tienen que ser del mismo taamaño")

    total = sum(multiplicacion)
    print(f"El resultado es {total}")



productoEscalar()