def suma_digitos(entrada: str) -> int:
    numeros: str = "0123456789"
    lista_numeros: list [int] = []
    sumatorio: int = 0
    for i in entrada:
        if i in numeros:
            lista_numeros.append(int(i))
    for j in lista_numeros:
        sumatorio += j
    return sumatorio
string: str = input("Dime un string con letras y números y te digo la suma de los números: ")
print(suma_digitos(string))