import os


def mostrar_tabla_multiplicar():
    # Solicita al usuario un número entre 1 y 10
    numero_ingresado = int(input("Ingrese un número entero entre 1 y 10: "))

    # Verifica si el número ingresado está dentro del rango válido
    if 1 <= numero_ingresado <= 10:
        # Define la ruta del directorio
        directorio = "Utils"

        # Define el nombre del archivo correspondiente al número ingresado
        nombre_archivo = f"tabla-{numero_ingresado}.txt"

        # Define la ruta completa del archivo
        ruta_archivo = os.path.join(directorio, nombre_archivo)

        # Verifica si el archivo existe
        if os.path.exists(ruta_archivo):
            # Abre el archivo y muestra su contenido por pantalla
            with open(ruta_archivo, 'r') as archivo:
                contenido = archivo.read()
                print(contenido)
        else:
            print("El archivo no existe.")
    else:
        print("Número inválido.")


# Llama a la función para mostrar la tabla de multiplicar
mostrar_tabla_multiplicar()
