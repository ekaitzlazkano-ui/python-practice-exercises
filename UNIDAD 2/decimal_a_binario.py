import math
def decimal_binario(decimal: int) -> int:
    binario: int = 0
    posicion: int = 0
    while decimal > 0:
        posicion = int(math.log2(decimal))
        binario += 10**posicion
        decimal -= 2**posicion
    return binario

decimal_user: int = int(input("Dime un número y te lo digo en binario: "))
resultado: int = decimal_binario(decimal_user)
print(f"Tu número en binario es {resultado}")