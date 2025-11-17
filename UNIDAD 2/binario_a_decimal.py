def binario_decimal(binario: str) -> int:
    decimal: int = 0
    for i in range(-1, -len(binario)-1, -1):
        if binario[i] == "1":
            decimal += (2**(abs(i)-1))
    return decimal
a: str = input("Dime un número en binario y te digo el decimal: ")
resultado = binario_decimal(a)
print(resultado)