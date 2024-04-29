import sqlite3
import datetime

class ProgramaGestionEmpleados:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd
        self.crear_tabla_empleados()

    def crear_tabla_empleados(self):
        try:
            # Conexión a la base de datos
            conn = sqlite3.connect(self.nombre_bd)
            cursor = conn.cursor()

            # Creación de la tabla de empleados
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS empleados (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    sueldo_base REAL NOT NULL,
                    afap TEXT NOT NULL,
                    fecha_ingreso TEXT NOT NULL,
                    cantidad_hijos INTEGER NOT NULL
                )
            ''')

            # Guardar cambios y cerrar conexión
            conn.commit()
            conn.close()

        except Exception as e:
            print("Error al crear la tabla de empleados:", str(e))

    def ingresar_empleado(self):
        try:
            nombre = input("Ingrese el nombre del empleado: ")
            apellido = input("Ingrese el apellido del empleado: ")
            sueldo_base = float(input("Ingrese el sueldo base del empleado: "))
            afap = input("Ingrese la AFP del empleado: ")
            fecha_ingreso = input("Ingrese la fecha de ingreso del empleado (YYYY-MM-DD): ")
            fecha_ingreso += ' 00:00:00'  # Agregar hora 00:00:00
            fecha_ingreso = datetime.datetime.strptime(fecha_ingreso, "%Y-%m-%d %H:%M:%S")
            cantidad_hijos = int(input("Ingrese la cantidad de hijos del empleado: "))

            # Conexión a la base de datos
            conn = sqlite3.connect(self.nombre_bd)
            cursor = conn.cursor()

            # Inserción de datos del empleado en la tabla
            cursor.execute('''
                INSERT INTO empleados (nombre, apellido, sueldo_base, afap, fecha_ingreso, cantidad_hijos)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (nombre, apellido, sueldo_base, afap, fecha_ingreso, cantidad_hijos))

            # Guardar cambios y cerrar conexión
            conn.commit()
            conn.close()

            print("Empleado ingresado correctamente.")

        except Exception as e:
            print("Error al ingresar empleado:", str(e))

    def calcular_pagos(self):
        try:
            # Conexión a la base de datos
            conn = sqlite3.connect(self.nombre_bd)
            cursor = conn.cursor()

            # Obtener datos de los empleados
            cursor.execute('''
                SELECT nombre, apellido, sueldo_base, afap, fecha_ingreso, cantidad_hijos
                FROM empleados
            ''')
            empleados = cursor.fetchall()

            total_fonasa = 0
            total_afap1 = 0
            total_afap2 = 0

            # Calcular pagos para cada empleado
            for empleado in empleados:
                nombre, apellido, sueldo_base, afap, fecha_ingreso_str, cantidad_hijos = empleado

                # Agregar hora 00:00:00 si no está presente
                if len(fecha_ingreso_str) == 10:
                    fecha_ingreso_str += ' 00:00:00'

                # Convertir la fecha de ingreso de str a datetime
                fecha_ingreso = datetime.datetime.strptime(fecha_ingreso_str, "%Y-%m-%d %H:%M:%S")

                # Cálculo de la base imponible
                bonificacion_meses = (datetime.datetime.now().year - fecha_ingreso.year) * 0.01
                asignacion_familiar = sueldo_base * cantidad_hijos * 0.05
                base_imponible = sueldo_base + sueldo_base * bonificacion_meses + asignacion_familiar

                # Descuento de FONASA
                descuento_fonasa = base_imponible * 0.07
                total_fonasa += descuento_fonasa

                # Descuento de AFAP
                if afap == "AFAP1":
                    descuento_afap = base_imponible * 0.12
                    total_afap1 += descuento_afap
                elif afap == "AFAP2":
                    descuento_afap = base_imponible * 0.114
                    total_afap2 += descuento_afap

                print(f"Empleado: {nombre} {apellido}, Pago a FONASA: {descuento_fonasa}, Pago a AFAP ({afap}): {descuento_afap}")

            # Calcular promedios de pagos
            cantidad_empleados = len(empleados)
            promedio_fonasa = total_fonasa / cantidad_empleados
            promedio_afap1 = total_afap1 / cantidad_empleados
            promedio_afap2 = total_afap2 / cantidad_empleados

            print(f"\nPromedio de pago a FONASA: {promedio_fonasa}")
            print(f"Promedio de pago a AFAP1: {promedio_afap1}")
            print(f"Promedio de pago a AFAP2: {promedio_afap2}")

            # Guardar cambios y cerrar conexión
            conn.commit()
            conn.close()

            print("Pagos calculados correctamente.")

        except Exception as e:
            print("Error al calcular pagos:", str(e))

    def ejecutar_programa(self):
        while True:
            print("\nMenú:")
            print("1. Ingresar empleado")
            print("2. Calcular pagos")
            print("3. Salir")

            opcion = input("Ingrese el número de la opción que desea realizar: ")

            if opcion == "1":
                self.ingresar_empleado()
            elif opcion == "2":
                self.calcular_pagos()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    programa = ProgramaGestionEmpleados('mi_base_de_datos.db')
    programa.ejecutar_programa()
