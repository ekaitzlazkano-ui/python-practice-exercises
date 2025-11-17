import random
numbers: list = []
a = random.randint(1,1000)
for i in range(1,101,1):
    numbers.append(a)
    while a in numbers:
        a = random.randint(1,1000)
user_number: int = int(input("Dime un número: "))
try:
    position: int = numbers.index(user_number)
    print(f"Tu número se encuentra en la posición {position+1}")
except:
    print("El número no pertenece a la lista")