import random
numeros_original: list [int] = []
numeros_resultado: list [int] = []

for i in range(100):
    numeros_original.append(random.randint(1,50))

for numero in numeros_original:
    if numero not in numeros_resultado:
        numeros_resultado.append(numero)
print(numeros_resultado)