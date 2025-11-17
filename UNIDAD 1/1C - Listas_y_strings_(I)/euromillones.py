import random
numeros: list[int] = []
estrellas: list [int] = []
while (len(numeros) < 5):
    aleatorio: int = random.randint(1, 50)
    if aleatorio not in numeros:
        numeros.append(aleatorio)

while len(estrellas) < 2:
    aleatorio: int = random.randint(1, 11)
    if aleatorio not in estrellas:
        estrellas.append(aleatorio)

print(f"{numeros}, estrellas: {estrellas}")