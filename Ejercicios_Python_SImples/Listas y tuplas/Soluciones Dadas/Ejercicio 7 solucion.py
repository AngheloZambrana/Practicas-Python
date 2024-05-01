def solucion1():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(alphabet), 1, -1):
        if i % 3 == 0:
            alphabet.pop(i - 1)
    print(alphabet)

def solucion2():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(alphabet), 1, -1):
        if i % 3 == 0:
            alphabet.pop(i - 1)
    print(alphabet)

solucion1()
#solucion2()