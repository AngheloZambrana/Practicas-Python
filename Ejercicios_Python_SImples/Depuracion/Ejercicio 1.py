contraseña = input('Introduce la contraseña: ') #Primer error ('Introduce la contraseña: ") esta cerrando mal las comillas
if contraseña in ['sesamo']:  #['sesamo'): esta cerrando un corchete con un parentesis
  print('Pasa')
else: #else no puso 2 puntos despues de la condicional
  print('No pasa')