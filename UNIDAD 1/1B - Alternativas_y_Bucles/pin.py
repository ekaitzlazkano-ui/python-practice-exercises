PIN: int = 7518
SALDO: int = 1527
intento: int = 0
i: int = 0

while i< 3:
    intento = int(input("PIN: "))
    if intento == PIN:
        print("PIN CORRECTO")
        print(f"Saldo: {SALDO}€")
        exit()
    else:
        print("PIN INCORRECTO")
        i = i + 1
print("TARJETA BLOQUEADA")