#metodos
class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.prdocuto = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(8, 2)
print(operacion.suma)
print(operacion.resta)
print(operacion.prdocuto)
print(operacion.division)