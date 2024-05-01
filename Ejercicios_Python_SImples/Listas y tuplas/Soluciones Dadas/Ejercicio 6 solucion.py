def solucion1():
    subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    passed = []
    for subject in subjects:
        score = float(input("¿Qué nota has sacado en " + subject + "?"))
        if score >= 5:
            passed.append(subject)
    for subject in passed:
        subjects.remove(subject)
    print("Tienes que repetir " + str(subjects))

def solucion2():
    subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    for i in range(len(subjects) - 1, -1, -1):
        score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
        if score >= 5:
            subjects.pop(i)
    print("Tienes que repetir " + str(subjects))

solucion1()
#solucion2()