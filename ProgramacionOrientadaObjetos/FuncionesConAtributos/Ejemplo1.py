#Funciones para atributos
class Persona:
    edad = 27
    nombre = 'victor'
    pais = 'Brazil'

doctor = Persona()
print(f"La edad del doctor es: {doctor.edad}")
print(f"La edad del doctor es: {getattr(doctor, 'edad')}")
print(f"El doctor tiene una edad de: {hasattr(doctor, 'edad')}") #True
print(doctor.nombre)
setattr(doctor, 'nombre', 'Hector') #Te modifica el atributo ya definido
print(doctor.nombre)
delattr(Persona, 'pais') #Te elimina un atributo

#getattr es una función en Python que se utiliza para obtener el valor de un atributo de un objeto dado su nombre.
# hasattr es una función en Python que se utiliza para verificar si un objeto tiene un atributo con un nombre específico.
# Devuelve True si el atributo está presente y False si no lo está.