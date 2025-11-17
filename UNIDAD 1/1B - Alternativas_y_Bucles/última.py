frase:str = input("Dime una frase y te diré solo la última palabra: ")
frase = frase[::-1]
palabra:str = ""

for i in frase:
    if i != " ":
        palabra += i
    else:
        break
palabra = palabra[::-1]
print(palabra)