def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia_palabras = {}
    for palabra in palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    return frecuencia_palabras

def palabra_mas_repetida(diccionario):
    palabra_mas_repetida = max(diccionario, key=diccionario.get)
    frecuencia_palabra_mas_repetida = diccionario[palabra_mas_repetida]
    return (palabra_mas_repetida, frecuencia_palabra_mas_repetida)

# Ejemplo de uso
cadena = input("Ingrese una cadena de caracteres: ")
frecuencia_palabras = contar_palabras(cadena)
print("Diccionario de frecuencia de palabras:", frecuencia_palabras)

palabra, frecuencia = palabra_mas_repetida(frecuencia_palabras)
print(f"La palabra más repetida es '{palabra}' con una frecuencia de {frecuencia} veces.")
