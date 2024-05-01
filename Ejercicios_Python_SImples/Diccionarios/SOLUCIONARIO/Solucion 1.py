def solucion1():
    monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
    moneda = input("Introduce una divisa: ")
    print(monedas.get(moneda.title(), "La divisa no está."))

def solucion():
    monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
    moneda = input("Introduce una divisa: ")
    if moneda.title() in monedas:
        print(monedas[moneda.title()])
    else:
        print("La divisa no está.")
solucion()