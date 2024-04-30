def fecha():
    dia = int(input("Ingrese el dia en el que haya nacido(dd): "))
    mes = int(input("Ingrese el mes en el que nacio(mm): "))
    año = int(input("Ingrese el año en el que nacio(yyyy): "))

    verificador = año / 1000

    if dia <= 31 and mes <= 12 and verificador > 1:
                print(f"Su fecha de nacimiento es {dia}/{mes}/{año}")
    else:
        print("El formato no es el correcto")

fecha()