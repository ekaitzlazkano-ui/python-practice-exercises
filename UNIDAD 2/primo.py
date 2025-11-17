import math
def es_primo(n: int) -> bool:
    raiz_n:int  = int(math.sqrt(n))
    primo: bool = False
    for i in range(raiz_n, 0, -1):
        if n%1==0 and n%n==0 and n%i==0:
            primo = False
            break
        else:
            primo = True
            break
    return primo
a: int = int(input("Dime un número y te diré si es primo: "))
numero_primo: bool = es_primo(a) 
print(numero_primo)       