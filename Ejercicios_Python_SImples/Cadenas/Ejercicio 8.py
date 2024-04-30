def separadorDecimales():
    precio_euros = float(input("Ingrese el precio del producto en euros con dos decimales: "))
    euros = int(precio_euros)
    centimos = int((precio_euros - euros) * 100)

    print(f"El precio ingresado es: {euros} euros y {centimos} céntimos")

separadorDecimales()

