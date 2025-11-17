def terminan_igual(palabra_1: str, palabra_2: str, n: int) -> bool:
        solucion: bool = True
        for i in range(-1, -n-1, -1):
            if palabra_1[i] != palabra_2[i]:
                solucion = False
        return solucion
palabra1: str = "Afición"
palabra2: str = "Camión"
indice: int = 3
resultado: bool = terminan_igual(palabra1, palabra2, indice)
print(resultado)