def divisa():
    divisas = {"Euro":'€', "Dollar":'$', "Yen":'¥'}
    opcion = input("Ingrese la divisa que quiere buscar (Euro, Dollar o Yen): ")
    if opcion in divisas:
        print(f"El símbolo de {opcion} es {divisas[opcion]}")
    else:
        print("La divisa no está en el diccionario.")

divisa()
