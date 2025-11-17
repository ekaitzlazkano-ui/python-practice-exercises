frase:str = input("Dime una frase y te diré la primera palabra: ")
for i in frase:
    if i != " ":
        print(i, end="")
    else:
        exit()