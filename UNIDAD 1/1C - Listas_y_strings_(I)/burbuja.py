import random
numeros: list[int] = []
for _ in range(10):
    numeros.append(random.randint(1,50))
print(numeros)
for n in range(len(numeros)-1):
    for i in range(len(numeros )-1 - n):
        elemento1:int = numeros[i]
        elemento2:int = numeros[i+1]
        if elemento2 < elemento1:
            numeros[i] = elemento2
            numeros[i+1] = elemento1

print(numeros)