def aplica_iva(base, iva = 21):  #Esta funcion se estaba creando debajo del print de la linea 6
    operacion = base * (1 + iva/100)   #La operacion para aplicar iva no era la correcta
    return operacion

base = float(input('Introduce la base imponible de la factura: ')) #Lo reconoce como String si no tiene el float antes del input
print(aplica_iva(base))  #No es necesario aqui llamar a iva si ya en la funccion ya la estas definiendo como parametro