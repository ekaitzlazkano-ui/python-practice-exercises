import string
abecedario: list [str] = list(string.ascii_lowercase)
morse: list [str] = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
frase: str = input("Dime una frase: ")
frase = frase.lower()
frase_morse: str = ""
for i in frase:
    if i in abecedario:
        a = abecedario.index(i)
        frase_morse += f"{morse[a]} "
print(frase_morse)