def desviacionTipica():
    numero = list(map(int, input("Ingrese su conjunto de numeros separado por ,:  ").split(',')))
    diferencias = []
    media = (sum(numero)) / len(numero)
    for i in range(len(numero) - 1):
        operacion = (numero[i] - media) ** 2
        diferencias.append(operacion)

    medio_diferencias = (sum(diferencias)) / len(diferencias)
    desviacion_tipica = medio_diferencias ** (1/2)
    print(f"Su media es {media} y su desviacion tipica es de {desviacion_tipica}")
desviacionTipica()