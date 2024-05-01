def fechaNacimiento():
    meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
        7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    dia = int(input("Ingrese el dia en el que haya nacido(dd): "))
    mes = int(input("Ingrese el mes en el que nacio(mm): "))
    año = int(input("Ingrese el año en el que nacio(yyyy): "))

    verificador = año / 1000

    if mes in meses and dia <= 31 and verificador > 1:
        print(f"{dia} de {meses[mes]} de {año}")
    else:
        print("El formato no es el correcto")

fechaNacimiento()