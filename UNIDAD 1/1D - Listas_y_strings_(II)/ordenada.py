numeros: list [int] = []
a: int = 1
esta_ordenada: bool = True

while a != 0:
    a = int(input("Dime un número y cuando no quieras añadir más números manda un 0: "))
    if a != 0:
        numeros.append(a)
for i in range(len(numeros)-1):
    if numeros[i] < numeros[i+1]:
        esta_ordenada = True
    else:
        esta_ordenada = False
        break
if esta_ordenada:
    print(f"{numeros} La lista está ordenada")
else:
    print(f"{numeros} La lista no está ordenada")