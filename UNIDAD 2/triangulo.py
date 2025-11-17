import estrellas_desde_hasta
        
def imprime_triangulo(altura: int):
    estrellas_desde_hasta.imprime_estrellas_lineas(1,altura)

altura_user: int = int(input("Qué altura quieres que tenga el triangulo? "))
imprime_triangulo(altura_user)