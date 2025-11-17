def dos_cuatro (numeros: list) -> bool:
    dos_xor_cuatro: bool = False
    counter: int = 0
    if 2 in numeros:
        counter += 1
    if 4 in numeros:
        counter += 1
    if counter%2 == 0:
        dos_xor_cuatro = False
    else:
        dos_xor_cuatro = True
    return dos_xor_cuatro

numeros_iniciales: list = [1, 3, 4, 5]
print(dos_cuatro(numeros_iniciales))