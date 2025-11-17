def parsea_entero(entrada: str) -> str:
    numeros: str = "0123456789"
    numero_final: str = ""
    for i in entrada:
        if i in numeros:
            numero_final += i
    return numero_final
string: str = input("Dime un string con letras y números y te devuelvo solo los números: ")
print(parsea_entero(string))