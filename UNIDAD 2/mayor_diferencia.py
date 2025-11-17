import math
def mayor_diferencia(numeros: list [int]) -> float:
    mayor = -math.inf
    menor = math.inf
    for numero in numeros:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    diferencia: float = mayor - menor
    return diferencia
lista_numeros: list [int] = [1,5,25,-4,12]
print(mayor_diferencia(lista_numeros))