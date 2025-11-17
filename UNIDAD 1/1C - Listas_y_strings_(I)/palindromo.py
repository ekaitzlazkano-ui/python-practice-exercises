sentence: str = input("Dime una frase: ")
sentence2 = sentence[::-1]
if sentence == sentence2:
    print("Tu frase es palindroma")
else:
    print("Tu frase no es palindroma")