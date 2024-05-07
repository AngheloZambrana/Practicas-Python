def producto_escalar(u, v):
    resultado = 0
    for i in range(len(u)):
        resultado += u[i] * v[i]
    return resultado

u = (1, 2, 3)
v = (4, 5, 6)
resultado = producto_escalar(u, v)
print(resultado)


# El bucle for intenta modificar los elementos de u, multiplicándolos por los elementos correspondientes
# de v, pero lo hace de manera incorrecta.