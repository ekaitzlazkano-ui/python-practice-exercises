numeros: list [int] = [1,4,6,9,12]
a: int = int(input("Dime un número: "))
for i in range(len(numeros)):
    if numeros[i] > a:
        print(f"El número hay que insertarlo en la posición {i}")
        numeros.insert(i, a)
        break
print(numeros)