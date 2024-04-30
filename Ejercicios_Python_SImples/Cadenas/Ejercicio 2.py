def tipoImpresiones():
    nombre_completo = str(input("Por favor, ingresa tu nombre completo: ").split())
    print(f"Nombre completo en minúsculas: {nombre_completo.lower()}")
    print(f"Nombre completo en mayusculas: {nombre_completo.upper()}")
    print(f"Nombre en formato de primera letra mayuscula {nombre_completo.title()}")

tipoImpresiones()