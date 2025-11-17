def matriz_identidad(dimension: int) -> list:
    result: list = []
    for i in range(dimension):
        actual_line: list = []
        for j in range(dimension):
            if j==i:
                actual_line.append(1)
            else:
                actual_line.append(0)
        result.append(actual_line)
    return result


matriz_result: list = matriz_identidad(4)
if __name__ == "__main__":
    for linea in matriz_result:
        print(linea)