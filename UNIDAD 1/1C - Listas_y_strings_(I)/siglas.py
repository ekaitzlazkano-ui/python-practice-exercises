frase: str = input("Dime una frase y te daré las siglas: ")
frase = frase.upper()
siglas:str = ""
check: bool = True
for i in frase:
    if check:
        siglas += i
        check = False
    if i == " ":
        check = True
print(siglas)