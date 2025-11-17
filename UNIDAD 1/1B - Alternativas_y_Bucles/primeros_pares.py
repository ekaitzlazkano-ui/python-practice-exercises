inicio = int(input("Dime el número de inicio: "))
fin = int(input("Dime el número final: "))
n_pares:int = 0
for i in range(inicio, fin+1):
    if i%2 == 0:
        print(i, end=" 7")
        n_pares += 1
    if n_pares >= 5:
        break