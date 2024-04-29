import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('mi_base_de_datos.db')
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
