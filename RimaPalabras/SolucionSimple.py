def rimas():
    palabra1 = input("Ingrese una palabra: ").lower()
    palabra2 = input("Ingrese su otra palabra: ").lower()

    ultimas_tres_letras_palabra1 = palabra1[-3:]
    ultimas_tres_letras_palabra2 = palabra2[-3:]

    ultimas_dos_letras_palabra1 = palabra1[-2:]
    ultimas_dos_letras_palabra2 = palabra2[-2:]

    if ultimas_tres_letras_palabra1 == ultimas_tres_letras_palabra2:
        print("Ambas palabras riman.")
    elif ultimas_dos_letras_palabra1 == ultimas_dos_letras_palabra2:
        print("Las palabras riman un poco.")
    else:
        print("Las palabras no riman.")

rimas()
