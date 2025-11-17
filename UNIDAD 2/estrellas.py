def imprime_estrellas(n) -> None:
    """función que imprime el número de * que queramos"""
    for _ in range(n):
        print("*", end ="")

a: int = int(input("Cuántas estrellas quieres? "))
imprime_estrellas(a)