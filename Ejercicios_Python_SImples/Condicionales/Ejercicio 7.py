def asingacionTipoImpositivo():
    rentaAnual = int(input("Ingrese el valor de su renta anual: "))
    if rentaAnual < 10000:
        print("Tipo impositivi de 5%")
    elif rentaAnual >= 10000 and rentaAnual < 20000:
        print("Tipo impositivi de 15%")
    elif rentaAnual >= 20000 and rentaAnual < 35000:
        print("Tipo impositivi de 20%")
    elif rentaAnual >= 35000 and rentaAnual < 60000:
        print("Tipo impositivi de 20%")
    elif rentaAnual >= 60000:
        print("Tipo impositivo de 45%")
asingacionTipoImpositivo()