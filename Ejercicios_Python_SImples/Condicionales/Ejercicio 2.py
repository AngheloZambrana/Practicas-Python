def verificadorContraseñas():
    cotraseña = "angheleckAZ"
    ingresada = input("Ingrese su contraseña: ")

    if ingresada.lower() == cotraseña.lower():
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")
verificadorContraseñas()