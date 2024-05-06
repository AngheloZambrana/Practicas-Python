def agregar_estudiante(estudiantes, nombre, tipo_beca, horas_trabajadas=None, calificacion=None):
    if nombre not in estudiantes:
        if tipo_beca == "Beca de Trabajo" and horas_trabajadas is None:
            horas_trabajadas = int(input(f"Ingrese las horas trabajadas para el estudiante {nombre}: "))
        elif tipo_beca == "Beca Académica" and calificacion is None:
            calificacion = float(input(f"Ingrese la calificación para el estudiante {nombre}: "))

        estudiantes[nombre] = {"tipo_beca": tipo_beca, "horas_trabajadas": horas_trabajadas,
                               "calificacion": calificacion}
        print(f"Estudiante {nombre} agregado.")
    else:
        print(f"El estudiante {nombre} ya está en la lista.")


def obtener_condiciones_beca(tipo_beca, becas):
    return becas.get(tipo_beca, {"condicion": 0, "tipo": "desconocido"})

def imprimir_estado_beca(estudiantes, nombre_estudiante, becas):
    if nombre_estudiante in estudiantes:
        estudiante = estudiantes[nombre_estudiante]
        tipo_beca = estudiante["tipo_beca"]
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


estudiantes = {}

agregar_estudiante(estudiantes, "Gaston", "Beca de Trabajo")
agregar_estudiante(estudiantes, "María", "Beca Académica")

becas = {
    "Beca Académica": {"condicion": 5, "tipo": "calificacion"},
    "Beca de Trabajo": {"condicion": 0, "tipo": "horas_trabajadas"}
}

imprimir_estado_beca(estudiantes, "Gaston", becas)
imprimir_estado_beca(estudiantes, "María", becas)
