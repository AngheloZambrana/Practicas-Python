def solucion():
    subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    scores = []
    for subject in subjects:
        score = input("¿Qué nota has sacado en " + subject + "?")
        scores.append(score)
    for i in range(len(subjects)):
        print("En " + subjects[i] + " has sacado " + scores[i])
solucion()