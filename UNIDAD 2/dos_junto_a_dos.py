def dos_junto_dos(numeros: list [int])-> bool:
    solucion: bool = False
    for i in range(len(numeros)-1):
            if numeros[i] == 2 and numeros[i] == numeros[i+1]:
                solucion = True
    return solucion

lista_numeros: list[int] = [0,1,2,2]
print(dos_junto_dos(lista_numeros))
