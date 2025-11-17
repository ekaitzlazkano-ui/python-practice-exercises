lista_original: list[str] = ["platano" , "piña", "manzana", "luz"]
lista_resultado: list [str] = []
print(lista_original)

for palabra in lista_original:
    if len(palabra) < 5:
        lista_resultado.append(palabra)
print(lista_resultado)