a = int(input("Dime un número y te digo su sumatorio desde 1 hasta tu número: "))
sumatorio: int=0
for i in range(1,a+1,1):
    sumatorio += i
print(f"El resultado es {sumatorio}")