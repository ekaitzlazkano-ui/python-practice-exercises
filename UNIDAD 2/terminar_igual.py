def terminan_igual(numeros_1: list[int], numeros_2: list[int], n: int) -> bool:
    if len(numeros_1) == len(numeros_2):
        solucion: bool = True
        for i in range(-1, -n-1, -1):
            if numeros_1[i] != numeros_2[i]:
                solucion = False
        return solucion
    else:
        print("Las listas no tienen la misma longitud")
        """Lo mismo que en mayor_lista.py"""
        return False
lista1: list [int] = [1,2,3,4]
lista2: list [int] = [0,2,3,4]
indice: int = 3
resultado: bool = terminan_igual(lista1, lista2, indice)
print(resultado)