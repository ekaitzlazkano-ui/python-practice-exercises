palabras: list [str] = ["platano", "piña", "manzana", "luz"]
abecedario_str: str = "abcdefghijklmnñopqrstuvwxyz"
abecedario: list [str] = list(abecedario_str)
lista_letras: list [str] = []
for i in range(len(palabras)):
    palabra: list [str] = list(palabras[i])
    for i in range(len(palabra)):
        lista_letras.append(palabra[i])
    palabra.clear()
print(lista_letras)
for i in range(len(lista_letras)):
    if lista_letras[i] in abecedario:
        abecedario.pop(abecedario.index(lista_letras[i]))
print(abecedario)