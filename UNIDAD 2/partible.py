def es_partible(lista: list[int])-> bool:
    suma: int = 0
    for numero in lista:
        suma += numero
    if suma%2 != 0:
        return False
    mitad: int = suma // 2
    suma_izquierda: int = 0
    for numero in lista:
        suma_izquierda = suma_izquierda+numero
        if suma_izquierda == mitad:
            return True
        elif suma_izquierda > mitad:
            