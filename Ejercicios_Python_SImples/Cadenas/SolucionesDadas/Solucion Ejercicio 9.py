def fecha():
    # Solicitar al usuario que ingrese la fecha de nacimiento
    fecha_str = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

    # Dividir la cadena en día, mes y año
    dia, mes, año = map(int, fecha_str.split('/'))

    # Verificar si el día, el mes y el año son válidos
    if 1 <= dia <= 31 and 1 <= mes <= 12 and año > 0:
        print(f"Su fecha de nacimiento es {dia:02d}/{mes:02d}/{año}")
    else:
        print("El formato no es correcto o la fecha no es válida")

fecha()
