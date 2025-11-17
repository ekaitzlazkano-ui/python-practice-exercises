import random
numbers: list = []
a = random.randint(1,1000)
for i in range(1,101,1):
    numbers.append(a)
    while a in numbers:
        a = random.randint(1,1000)
number_min: int = min(numbers)
number_max: int = max(numbers)
difference: int = number_max - number_min
print(f"El rango de amplitud de los números de la lista es de {difference}")