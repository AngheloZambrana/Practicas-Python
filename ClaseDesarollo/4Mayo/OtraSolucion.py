def agregar_estudiante(estudiantes, nombre, tipo_beca, horas_trabajadas=None, calificacion=None):
    if nombre not in estudiantes:
        estudiantes[nombre] = {"tipo_beca": tipo_beca, "horas_trabajadas": horas_trabajadas,
                               "calificacion": calificacion}
        print(f"Estudiante {nombre} agregado.")
    else:
        print(f"El estudiante {nombre} ya está en la lista.")


def verificar_estudiante(estudiantes, nombre):
    return nombre in estudiantes


def verificar_viabilidad_beca(estudiante, becas):
    tipo_beca = estudiante.get("tipo_beca")
    if tipo_beca in becas:
        condicion = becas[tipo_beca]["condicion"]
        tipo_condicion = becas[tipo_beca]["tipo"]
        valor_condicion = estudiante.get(tipo_condicion)

        if valor_condicion is not None:
            return valor_condicion >= condicion
        else:
            return False
    else:
        print(f"El estudiante tiene una beca de tipo desconocido: {tipo_beca}")
        return False


def imprimir_estado_beca(estudiantes, nombre_estudiante, becas):
    if nombre_estudiante in estudiantes:
        estudiante = estudiantes[nombre_estudiante]
        tipo_beca = estudiante.get("tipo_beca")
        detalles_beca = estudiante
        if tipo_beca in becas:
            condicion = becas[tipo_beca]["condicion"]
            tipo_condicion = becas[tipo_beca]["tipo"]
            valor_condicion = detalles_beca.get(tipo_condicion)
            if valor_condicion is not None:
                if tipo_condicion == "calificacion" and valor_condicion >= condicion:
                    print(
                        f"El estudiante {nombre_estudiante} tiene una {tipo_beca} y su {tipo_condicion} es {valor_condicion}.")
                elif tipo_condicion == "horas_trabajadas" and valor_condicion >= condicion:
                    print(
                        f"El estudiante {nombre_estudiante} tiene una {tipo_beca} y ha trabajado {valor_condicion} horas.")
                else:
                    print(f"El estudiante {nombre_estudiante} ya no cumple con los requisitos para la {tipo_beca}.")
            else:
                print(
                    f"El estudiante {nombre_estudiante} tiene una {tipo_beca} pero no se ha registrado {tipo_condicion}.")
        else:
            print(f"El estudiante {nombre_estudiante} tiene una beca de tipo desconocido.")
    else:
        print(f"No se encontró al estudiante {nombre_estudiante} en la lista.")


def agregar_nueva_beca(becas, nombre_beca, condicion, tipo):
    becas[nombre_beca] = {"condicion": condicion, "tipo": tipo}
    print(f"Beca '{nombre_beca}' agregada al sistema.")


def mostrar_menu():
    print("Bienvenido al sistema de gestión de becas estudiantiles")
    print("1. Añadir estudiante")
    print("2. Verificar estudiante")
    print("3. Verificar viabilidad de beca para un estudiante")
    print("4. Agregar nueva beca")
    print("5. Ver estado de beca de un estudiante")
    print("6. Salir")


def main():
    estudiantes = {}
    becas = {
        "Beca Académica": {"condicion": 5, "tipo": "calificacion"},
        "Beca de Trabajo": {"condicion": 100, "tipo": "horas_trabajadas"}
    }

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            tipo_beca = input("Ingrese el tipo de beca (Beca Académica / Beca de Trabajo): ")
            if tipo_beca not in ["Beca Académica", "Beca de Trabajo"]:
                print("Tipo de beca no válido.")
                continue
            horas_trabajadas = None
            calificacion = None
            if tipo_beca == "Beca de Trabajo":
                horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
            else:
                calificacion = float(input("Ingrese la calificación: "))
            agregar_estudiante(estudiantes, nombre, tipo_beca, horas_trabajadas, calificacion)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante que desea verificar: ")
            print(verificar_estudiante(estudiantes, nombre))
        elif opcion == "3":
            nombre = input("Ingrese el nombre del estudiante para verificar la viabilidad de su beca: ")
            print(verificar_viabilidad_beca(estudiantes.get(nombre, {}), becas))
        elif opcion == "4":
            nombre_beca = input("Ingrese el nombre de la nueva beca: ")
            condicion = int(input("Ingrese la condición de la nueva beca: "))
            tipo = input("Ingrese el tipo de condición (calificacion / horas_trabajadas): ")
            agregar_nueva_beca(becas, nombre_beca, condicion, tipo)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del estudiante para ver el estado de su beca: ")
            imprimir_estado_beca(estudiantes, nombre, becas)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()
