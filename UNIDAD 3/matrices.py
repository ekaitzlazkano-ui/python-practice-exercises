def suma(matriz_1: list, matriz_2: list) -> list:
    result: list = []
    for i in range(len(matriz_1)):
        actual_line: list = []
        for j in range(len(matriz_1[0])):
            actual_line.append(matriz_1[i][j]+matriz_2[i][j])
        result.append(actual_line)
    return result

def producto(matriz_1: list, matriz_2: list) -> list:
    result: list = []
    for i in range(len(matriz_1)):
        actual_line: list = []
        for k in range(len(matriz_2)):
            actual_value: int = 0
            for j in range(len(matriz_2[0])):
                actual_value += (matriz_1[i][j] * matriz_2[j][k])
            actual_line.append(actual_value)
        result.append(actual_line)
    return result


matriz_1: list[list] = [
[2,0,1],
[0,-1,-1],
[1,3,0]
]

matriz_2: list[list] =[
[2,0,2],
[-1,0,1],
[0,3,0]
]

matriz_suma: list = suma(matriz_1, matriz_2)
matriz_producto: list = producto(matriz_1, matriz_2)

if __name__ == "__main__":
    for linea in matriz_suma:
        print(linea)
    print()
    for linea in matriz_producto:
        print(linea)