def solucion1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(1, 11):
        print(numbers[-i], end=", ")

def solucion2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers.reverse()
    for number in numbers:
        print(number, end=", ")

solucion1()
solucion2()
