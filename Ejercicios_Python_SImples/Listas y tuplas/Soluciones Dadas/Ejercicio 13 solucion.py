def solucion():
    sample = input("Introduce una muestra de números separados por comas: ")
    sample = sample.split(',')
    n = len(sample)
    for i in range(n):
        sample[i] = int(sample[i])
    sample = tuple(sample)
    sum = 0
    sumsq = 0
    for i in sample:
        sum += i
        sumsq += i ** 2
    mean = sum / n
    stdev = (sumsq / n - mean ** 2) ** (1 / 2)
    print('La media es', mean, ', y la desviación típica es', stdev)
solucion()