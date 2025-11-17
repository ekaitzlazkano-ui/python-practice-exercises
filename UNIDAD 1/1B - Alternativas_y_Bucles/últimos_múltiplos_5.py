a = int(input("Dime un número de inicio: "))
b = int(input("Dime un número final: "))
números:list[int] = []

for i in range(a, b+1, 1):
    if i%5 == 0:
        números.append(i)
print(números[-3:])