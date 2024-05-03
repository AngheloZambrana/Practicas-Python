def convertirDiccionario(lista):
    diccionario = {}
    for palabra in lista:
        longitud = len(palabra)
        diccionario[palabra] = longitud
    return diccionario

lista = input("Ingrese su lista de palabras separadas por espacios: ").split()
resultado = convertirDiccionario(lista)
print(f"El diccionario de la lista es: {resultado}")
