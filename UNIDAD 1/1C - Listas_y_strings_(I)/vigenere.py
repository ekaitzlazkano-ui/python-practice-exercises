import string
abecedario: list [str] = list(string.ascii_uppercase)
texto: str = input("Texto: ")
texto = texto.upper()
clave: str = input("Clave: ")

texto_cifrado: str = ""
for i in range(len(texto)):
    letra: str = texto[i]
    if letra in abecedario:
        indice_clave : int =  i % len(clave)
        desplazamiento = int(clave[indice_clave])
        indice_original: int = abecedario.index(letra)
        indice_cifrado: int = (indice_original + desplazamiento) % len(abecedario)
        letra_cifrada: str = abecedario[indice_cifrado]
        texto_cifrado += letra_cifrada
    else:
        texto_cifrado += letra
print(texto_cifrado)