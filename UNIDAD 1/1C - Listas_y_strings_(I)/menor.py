import random
numbers: list = []
a = random.randint(1,1000)
for i in range(10):
    numbers.append(a)
    while a in numbers:
        a = random.randint(1,1000)

#forma para no usar la función min() propia de python
menor:int = 1001
b:int = 0
position:int = 0
for number in numbers:
    b += 1
    if number < menor:
        menor = number
        position = b

print(f"El número más pequeño de la lista es el {menor} y se encuentra en la posición {position}")