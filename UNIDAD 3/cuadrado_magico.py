from limpia_matrices import matriz_transpuesta

def cuadrado_magico(matriz:list[list]) -> bool:
    valores: list = []
    for fila in matriz:
        valores.append(sum(fila))
    transpuesta: list = matriz_transpuesta(matriz)
    for fila in transpuesta:
        valores.append(sum(fila))
    if min(valores) == max(valores):
        return True
    return False


if __name__ == "__main__":
    matriz: list[list] = [
[0,1,0],
[0,0,1],
[1,0,0]
]
    resultado = cuadrado_magico(matriz)
    print(resultado)