def solucion():
    persona = {}
    continuar = True
    while continuar:
        clave = input('¿Qué dato quieres introducir? ')
        valor = input(clave + ': ')
        persona[clave] = valor
        print(persona)
        continuar = input('¿Quieres añadir más información (si/no)? ').lower() == "si"

solucion()