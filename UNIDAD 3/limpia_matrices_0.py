def matriz_transpuesta(matriz: list[list]) -> list:
    result: list [list] = []
    for i in range(len(matriz[0])):
        actual_line: list = []
        for j in range(len(matriz)):
            actual_line.append(matriz[j][i])
        result.append(actual_line)
    return result

def clean_zero_horiz(matriz: list[list]) -> list:
    result: list[list] = []
    for fila in matriz:
        if sum(fila) != 0:
            result.append(fila)
    return result

            
if __name__ == "__main__":
    matriz: list[list] = [
[0,0,0,0],
[5,2,0,3],
[2,0,0,1],
[5,2,0,0]
]
    for _ in range(2):
        matriz = clean_zero_horiz(matriz)
        matriz = matriz_transpuesta(matriz)
    for linea in matriz:
        print(linea)