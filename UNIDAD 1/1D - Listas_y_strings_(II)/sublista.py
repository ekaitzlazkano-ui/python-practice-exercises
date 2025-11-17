import random
lista: list [int] = [1,2,3,4,5,6,7]
sublista: list [int] = [1,2, 3]
print(lista)
print(sublista)

es_sublista: bool = False
for i in range(len(lista) - len(sublista) + 1):
    lista_b: list [int] = lista[i:i+len(sublista)]
    if lista_b == sublista:
        es_sublista = True
        break
if es_sublista:
    print("b es una sublista de a")
else:
    print("b no es una sublista de a")