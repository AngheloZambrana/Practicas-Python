def solucion():
    word = input("Introduce una palabra: ")
    vocals = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocals:
        times = 0
        for letter in word:
            if letter == vocal:
                times += 1
        print("La vocal " + vocal + " aparece " + str(times) + " veces")

solucion()