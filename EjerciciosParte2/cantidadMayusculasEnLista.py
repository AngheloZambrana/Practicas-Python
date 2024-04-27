#Escribir un programa que le diga al usuario que ingrese una cadena.
# El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene

def mayusculas_Lista(lista):
    contador = 0
    for palabra in lista:
        for letra in palabra:
            if letra.isupper():
                contador += 1
    return contador

lista = input("Ingrese su lista de datos separados por espacios: ").split()
resultado = mayusculas_Lista(lista)
print("La cadena tiene", resultado, "letras mayúsculas.")

