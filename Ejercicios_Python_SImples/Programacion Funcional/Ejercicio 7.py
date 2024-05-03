def AsignarCalificaciones(diccionario):
    diccionarioTraducido = {}
    for valor in diccionario.keys():
        clave = diccionario[valor]
        if clave < 0 or clave > 10:
            print(f"Nota {clave} fuera del rango válido (0 a 10).")
            diccionarioTraducido[valor] = None
        elif clave >= 9:
            diccionarioTraducido[valor] = 'A'
        elif 8 <= clave < 9:
            diccionarioTraducido[valor] = 'B'
        elif 7 <= clave < 8:
            diccionarioTraducido[valor] = 'C'
        elif 6 <= clave < 7:
            diccionarioTraducido[valor] = 'D'
        else:
            diccionarioTraducido[valor] = 'F'
    return diccionarioTraducido

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