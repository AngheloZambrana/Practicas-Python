def AsignarCalificaciones(diccionario):
    diccionarioAprobados = {}
    for valor in diccionario.keys():
        clave = diccionario[valor]
        if clave >= 9:
            diccionarioAprobados[valor] = 'A'
        elif 8 <= clave < 9:
            diccionarioAprobados[valor] = 'B'
        elif 7 <= clave < 8:
            diccionarioAprobados[valor] = 'C'
        elif 6 <= clave < 7:
            diccionarioAprobados[valor] = 'D'
    if diccionarioAprobados:
        return diccionarioAprobados
    else:
        return {}


def crearDiccionario(numero):
    diccionario = {}
    for i in range(numero):
        valor = input("Ingrese la Asignatura que desee añadir: ")
        clave = int(input("Ingrese la nota en el rango de 1 al 10: "))
        if clave > 0 or clave < 10:
            diccionario[valor.upper()] = clave
    return diccionario

contador = int(input("Ingrese la longitud de su diccionario: "))
finalDiccionario = crearDiccionario(contador)
resultado = AsignarCalificaciones(finalDiccionario)
print(f"El diccionario con calificaciones aplicadas sería: {resultado}")