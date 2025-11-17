def filas(dimension: int) -> list:
    """Crea un cubo de las dimensiones que le digas"""
    resultado: list = []
    sub_lista: list = []
    for i in range(dimension):
        numero: int = i+1
        for _ in range(dimension):
            sub_lista.append(numero)
        resultado.append(sub_lista)
        sub_lista = []
    return resultado


if __name__ == "__main__":
    resultado: list = filas(9)
    for i in range(len(resultado)):
        print(resultado[i])