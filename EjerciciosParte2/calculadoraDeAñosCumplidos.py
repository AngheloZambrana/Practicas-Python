#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

def calculadoraEdad():
    año_curso = int(input("Ingrese el año en curso: "))
    nombre = input("Ingrese el nombre de la persona: ")
    año = int(input("Ingrese el año de naciiento: "))
    if año < año_curso:
        resultado = año_curso - año
        print(nombre, "cumple", resultado, "este año")
    else:
        print("Aun no nacio")

calculadoraEdad()