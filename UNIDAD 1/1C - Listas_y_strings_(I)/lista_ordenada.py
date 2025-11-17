numeros:list[int] = []
anterior: int = 0
while len(numeros)<10:
    numero: int = int(input("Dime un número: "))
    if numero >= anterior:
        numeros.append(numero)
        anterior = numero
    else:
        print("ERROR")
print(numeros)