a = int(input("Dime un número de inicio: "))
b = int(input("Dime un número final: "))
factorial:int = 1

for rango in range(a,b+1):
    for i in range(rango, 0, -1):
        factorial *= i
    print(factorial)
    factorial = 1