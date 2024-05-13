#Herencia

class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return '{} es un pokemon de tipo: {}'.format(self.nombre, self.tipo)

class Pikachu(Pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)

class Charmander(Pokemon):
    def ataque(self, tipoataque):
        return '{}  tipo de ataque: {}'.format(self.nombre, tipoataque)

nuevo_pokemon = Pikachu('Bobby', 'Electrico')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('Electrico'))
