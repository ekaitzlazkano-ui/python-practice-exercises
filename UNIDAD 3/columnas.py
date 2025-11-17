def columnas(dimension: int) -> list:
    sublista: list = []
    resultado: list = []
    for i in range(dimension):
        sublista.append(i+1)
    for i in range(dimension):
        resultado.append(sublista)
    return resultado

resultado: list = columnas(9)
for i in range(len(resultado)):
    print(resultado[i])
    