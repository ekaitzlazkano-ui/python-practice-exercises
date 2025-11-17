import string
abecedario: list [str] = list(string.ascii_uppercase)
frase:str = input("Dime una frase: ")
frase = frase.upper()
desplazamiento:int = int(input("Dime un desplazamiento: "))
nueva_frase:str = ""

for i in frase:
    if i in abecedario:
        indice_original: int = abecedario.index(i)
        indice_cifrado: int = (indice_original + desplazamiento)%len(abecedario)
        letra_cifrada = abecedario[indice_cifrado]
        nueva_frase += letra_cifrada
    else:
        nueva_frase += i
print(f"Cifrado: {nueva_frase}")