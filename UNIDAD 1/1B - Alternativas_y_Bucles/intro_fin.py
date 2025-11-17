i = 0
while i == 0:
    a: str = str(input("Dime un nombre: "))
    print(f"Has escrito: {a}")
    a = a.lower()
    if a == "fin":
        break