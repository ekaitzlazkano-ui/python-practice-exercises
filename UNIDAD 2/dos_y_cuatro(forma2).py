def dos_y_cuatro(numeros:list) -> bool:
    return ((2 in numeros) or (4 in numeros)) and not((2 in numeros) and (4 in numeros))

numeros_iniciales: list = [1, 3, 4, 5]
print(dos_y_cuatro(numeros_iniciales))