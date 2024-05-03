def AsignarCalificaciones(lista_numeros):
    calificaciones = []
    for nota in lista_numeros:
        if nota < 0 or nota > 10:
            print(f"Nota {nota} fuera del rango válido (0 a 10).")
            calificaciones.append(None)
        if nota >= 9:
            calificaciones.append('A')
        elif 8 <= nota < 9:
            calificaciones.append('B')
        elif 7 <= nota < 8:
            calificaciones.append('C')
        elif 6 <= nota < 7:
            calificaciones.append('D')
        else:
            calificaciones.append('F')
    return calificaciones

entrada = input("Ingresa la lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]
resultado = AsignarCalificaciones(numeros)
print(f"La lista con funcion aplicada seria {resultado}")