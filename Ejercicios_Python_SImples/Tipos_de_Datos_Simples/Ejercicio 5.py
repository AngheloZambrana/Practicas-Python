#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.
def pagoPorHora():
    hora = int(input("Ingrese el numero de horas trabajadas: "))
    costo = int(input("Ingrese el costo por hora: "))
    paga = hora * costo
    print(f"Si trabaja {hora} horas y le pagan {costo}$ por hora, su paga es de {paga}$")
pagoPorHora()