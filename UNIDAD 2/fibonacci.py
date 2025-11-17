def fibonacci(n) -> int:
    a: int = 0
    b: int = 1
    resultado: int = 0
    for _ in range(n):
        if a<b:
            resultado = a
            a = a+b
        else:
            resultado = b
            b = a+b
    return resultado
a: int = int(input("Dime un número y te dire ese enésimo fibonacci: "))
numero: int = fibonacci(a)
print(numero)