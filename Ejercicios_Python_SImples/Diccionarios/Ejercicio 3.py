def ventaFruta():
    fruta = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}
    pedido = input("Ingrese la fruta que desea comprar: ").capitalize()
    kilos = int(input("Ingrese la cnatidad de kilos que desea comprar: "))
    if pedido in fruta:
        total = kilos * fruta[pedido]
        print(f"Compro {kilos}kg de {pedido} su total es de {total}")
    else:
        print("No tenemos esa fruta actualmente")

ventaFruta()