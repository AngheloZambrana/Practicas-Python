def creditosCurso():
    asignaturas = {"Matemáticas": 6, "Física": 4, "Química": 5}
    total_creditos = 0
    for materia, credito in asignaturas.items():
        print(f"{materia} tiene {credito} creditos")
        total_creditos += credito
    print('Número total de créditos del curso: ', total_creditos)


creditosCurso()