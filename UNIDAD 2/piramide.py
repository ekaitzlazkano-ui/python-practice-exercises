def imprime_estrellas_lineas(desde: int, hasta: int) -> None:
    veces: int = (hasta-desde)+1
    for i in range(veces):
        print(" "*((hasta-1)-i), end="")
        for _ in range((desde + i)):
            print("*", end="")
        print("*"*i, end="")
        print()

def imprime_piramide(altura: int):
    imprime_estrellas_lineas(1,altura)

altura_user: int = int(input("Qué altura quieres que tenga la piramide? "))
imprime_piramide(altura_user)