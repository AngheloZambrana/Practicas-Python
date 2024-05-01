def contadorVocales():
    palabra = input("Ingrese la palabra que desee: ")
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    for i in range(len(palabra)):
        if palabra[i] == "a":
            contador_a += 1
        elif palabra[i] == "e":
            contador_e += 1
        elif palabra[i] == "i":
            contador_i += 1
        elif palabra[i] == "o":
            contador_o += 1
        elif palabra[i] == "u":
            contador_u += 1
    print(f"Su palabra tiene {contador_a} letras a")
    print(f"Su palabra tiene {contador_e} letras e")
    print(f"Su palabra tiene {contador_i} letras i")
    print(f"Su palabra tiene {contador_o} letras o")
    print(f"Su palabra tiene {contador_u} letras u")


contadorVocales()