fila1: list[str] = ["Jon", "Iker", "Ander"]
fila2:list[str] = ["Ekaitz", "Unai", "Ane"]
fila3:list[str] = ["Oier", "Diego", "Javi"]

clase:list = [fila1, fila2, fila3]

fila: int = int(input("Dime una fila: "))
fila_menosuno: int = fila -1

asiento: int = int(input("Dime un asiento: "))
asiento_menosuno = asiento -1

print(f"En la fila {fila}, asiento {asiento}, se sienta {clase[fila_menosuno][asiento_menosuno]}")