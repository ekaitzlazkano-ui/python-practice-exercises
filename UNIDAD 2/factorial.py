def factorial(n) -> int:
    fact: int = 1
    for i in range(n):
        fact *= (i+1)
    return fact
a: int = int(input("Dime un número y te digo su factorial: "))
resultado: int = factorial(a)
print(resultado)