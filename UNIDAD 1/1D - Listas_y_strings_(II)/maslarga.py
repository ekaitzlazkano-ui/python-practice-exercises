frase: str = input("Dime una frase y te diré la palabra más larga: ")
palabras: list [str] = frase.split()
larga: str = ""

for palabra in palabras:
    if len(palabra) > len(larga):
        larga = palabra
print(larga)