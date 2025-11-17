import random
veces: list [int] = [0,0,0,0,0,0]
n: int = int(input("Dime cuántas veces quieres que tire el dado: "))
tirada: int = 0

for _ in range(n):
    tirada = random.randint(1,6)
    for i in range(6):
        if tirada == i+1:
            veces[i] +=1
print(veces)
for i in range(6):
    print(f"El numero {i+1} ha salido un {((veces[i]/n)*100):.2f}% de las veces")