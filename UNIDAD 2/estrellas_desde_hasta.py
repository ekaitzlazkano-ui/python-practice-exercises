def imprime_estrellas_lineas(desde: int, hasta: int) -> None:
    veces: int = (hasta-desde)+1
    for i in range(veces):
        for _ in range((desde + i)):
            print("*", end="")
        print()
        
inicio: int = int(input("Dime el número de inicio: "))
fin: int = int(input("Dime el número de fin: "))
imprime_estrellas_lineas(inicio, fin)