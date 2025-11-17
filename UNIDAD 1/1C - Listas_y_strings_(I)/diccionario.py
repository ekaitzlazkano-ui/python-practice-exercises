palabra1: str = input("Primera: ")
palabra2: str = input("Segunda: ")

if palabra1 < palabra2:
    print(f"La palabra {palabra1} está antes en el diccionario")
elif palabra1 > palabra2:
    print(f"La palabra {palabra2} está antes en el diccionario")
else:
    print("Me has dicho dos veces la misma palabra.")