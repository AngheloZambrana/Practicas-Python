def calculoPrecio(lista_diccionarios):
    lista_costos = []
    for i in range(len(lista_diccionarios)):
        diccionario_seleccionado = lista_diccionarios[i]
        if diccionario_seleccionado['zona'] == 'A':
            metros = diccionario_seleccionado['metros']
            habitaciones = diccionario_seleccionado['habitaciones']
            if diccionario_seleccionado['garaje']:
                garaje = 500
            else:
                garaje = 1
            antiguedad = 2024 - diccionario_seleccionado['año']
            costo = (metros * 1000 + habitaciones * 500 + garaje * 15000) * (1 - antiguedad/100) * 1.5
            lista_costos.append(costo)
        elif diccionario_seleccionado['zona'] == 'B':
            metros = diccionario_seleccionado['metros']
            habitaciones = diccionario_seleccionado['habitaciones']
            if diccionario_seleccionado['garaje']:
                garaje = 500
            else:
                garaje = 1
            antiguedad = 2024 - diccionario_seleccionado['año']
            costo = (metros * 100 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad/100) * 1.5
            lista_costos.append(costo)
        else:
            print("Tu zona no existe")
    return lista_costos
def MejoresOfertas(lista_diccionarios, lista_precios,precio):
    lista_final = []
    for i in range(len(lista_diccionarios)):
        if lista_precios[i] <= precio:
            lista_final.append(lista_diccionarios[i])
    return lista_final


Lista_diccionario = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

PrecioTotal = calculoPrecio(Lista_diccionario)
print(f"La lista de precios de las ofertas son {PrecioTotal}")
precio_usuario = float(input("Ingrese el precio que desea comparar: "))
resultado = MejoresOfertas(Lista_diccionario, PrecioTotal,precio_usuario)
print(f"Las mejores ofertas segun el precio que pide son {resultado}")