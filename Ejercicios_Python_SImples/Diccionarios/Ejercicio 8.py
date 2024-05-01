def traductor():
    diccionario_espanol_ingles = {"Hola": "Hello", "mi": "my", "nombre": "name", "es": "is", "un": "a", "poco": "little", "mucho": "much"}
    frase = input("Ingrese su lista de datos separados por espacios: ").split()
    frase_traducida = []
    for i in range(len(frase)):
        if frase[i] in diccionario_espanol_ingles:
            frase_traducida.append(diccionario_espanol_ingles[frase[i]])
        else:
            frase_traducida.append(frase[i])

    frase_final = " ".join(frase_traducida)
    print(frase_final)

traductor()