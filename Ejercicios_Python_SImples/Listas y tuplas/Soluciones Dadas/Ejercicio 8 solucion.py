def solucion():
    word = input("Introduce una palabra: ")
    reversed_word = word
    word = list(word)
    reversed_word = list(reversed_word)
    reversed_word.reverse()
    if word == reversed_word:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")

solucion()