lista_resultado: list [int] = []
for numero in range(1,101):
    if numero%2 == 0 or numero%3 == 0 or numero%5 == 0 or numero%7 == 0:
        lista_resultado.append(numero)
print(lista_resultado)