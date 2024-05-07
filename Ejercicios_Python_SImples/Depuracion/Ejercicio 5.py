def producto(a, b):
    producto = []
    for i in range(len(a)):
        fila = []
        for j in range(len(b[0])):
            suma = 0
            for k in range(len(b)):
                suma += a[i][k] * b[k][j]
            fila.append(suma)
        producto.append(tuple(fila))
    return tuple(producto)

a = ((1, 2, 3),
     (3, 2, 1))
b = ((1, 2),
     (3, 4),
     (5, 6))
result = producto(a, b)
print(result)

## El error principal en la implementación original estaba en el bucle interno donde se calculaba la suma de los productos de los elementos de las filas y columnas. En particular, en esta línea:
# python
# suma += a[i][k] * b[k+1][j]
# El índice k+1 en b[k+1][j] estaba desplazado, lo cual provocaba que el bucle intentara acceder a índices fuera de rango y generara un error. Además, había otros problemas de indexado incorrecto y asignación de valores en listas que causaban errores adicionales.