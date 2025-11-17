frase: str = input("Dime una frase y te diré cuántes consonantes tiene: ")
frase = frase.lower()
n: int = 0
for i in frase:
    if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and i != " ":
        n += 1
print(f"Tu frase tiene {n} vocales")