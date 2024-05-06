class Titere:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return ""

    def bailar(self):
        return ""

    def saltar(self):
        return ""

    def cantar(self):
        return ""

    def robar(self):
        return ""

class TitereJheremy(Titere):
    def saludar(self):
        return (f"{self.nombre}: Volviendo de la sansi pasen tareas")
class TiterePrincesa(Titere):
    def saludar(self):
        return f"{self.nombre}: ¡Ya llegué!"

class TitereRey(Titere):
    def saludar(self):
        return f"{self.nombre}: ¡Saludos, súbditos!"

class TitereMozo(Titere):
    def saludar(self):
        return f"{self.nombre}: ¡Buen día, señores y señoras!"

class TitereLadron(Titere):
    def saludar(self):
        return ""  # El ladrón no saluda
    def robar(self):
        return f"{self.nombre}: Oh no el ladron se robo mis panqueques"

class Titiritero:
    def __init__(self, titere):
        self.titere = titere

    def realizar_accion(self, accion):
        if accion == "saludar":
            return self.titere.saludar()
        elif accion == "bailar":
            return self.titere.bailar()
        elif accion == "saltar":
            return self.titere.saltar()
        elif accion == "cantar":
            return self.titere.cantar()
        elif accion == "robar":
            return self.titere.robar()

titere_princesa = TiterePrincesa("Princesa")
titere_rey = TitereRey("Rey")
titere_mozo = TitereMozo("Mozo")
titere_ladron = TitereLadron("Ladrón")
titere_jheremy = TitereJheremy("JheremyGod")

titiritero =Titiritero(titere_jheremy)
print(titiritero.realizar_accion("saludar"))

titiritero = Titiritero(titere_princesa)
print(titiritero.realizar_accion("saludar"))

titiritero.titere = titere_rey
print(titiritero.realizar_accion("saludar"))

titiritero.titere = titere_mozo
print(titiritero.realizar_accion("saludar"))

titiritero.titere = titere_ladron
print(titiritero.realizar_accion("robar"))
