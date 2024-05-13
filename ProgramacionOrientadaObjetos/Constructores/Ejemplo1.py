#metodo constructor

class Persona:
    pass
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    def descripcion(self):
        return '{} tiene {}'. format(self.nombre, self.año)

    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre, frase)

doctor = Persona('Jose', 26)
print(doctor.descripcion())
print(doctor.comentario('Hola que tal'))