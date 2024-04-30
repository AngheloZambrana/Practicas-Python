def numerosTelefonicos():
    prefijo = input("Ingrese el prefijo de su teléfono (+34): ")
    numero = input("Ingrese el número de su teléfono (9 dígitos): ")
    extension = input("Ingrese la extensión de su teléfono (2 dígitos): ")

    if len(prefijo) == 3 and len(numero) == 9 and len(extension) == 2:
        numero_sin_prefijo_extension = numero
        print(f"Número de teléfono sin prefijo ni extensión: {numero_sin_prefijo_extension}")
    else:
        print("Formato incorrecto")

numerosTelefonicos()
