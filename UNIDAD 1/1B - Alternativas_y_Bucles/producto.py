a = int(input("Dime un número y te digo su producto desde 1 hasta tu número: "))
producto:int= 1
for i in range(1,a+1,1):
    producto *= i
print(f"El resultado es {producto}")