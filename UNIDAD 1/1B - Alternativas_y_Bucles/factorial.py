a = int(input("Dime un número y te digo su producto desde 1 hasta tu número: "))
factorial:int = 1
for i in range(a,0,-1):
    factorial *= i
print(f"El resultado es {factorial}")