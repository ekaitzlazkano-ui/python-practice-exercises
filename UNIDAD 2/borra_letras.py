def borra_letras (string_1: str, string_2: str) -> str:
    resultado: str = ""
    for letra in string_1:
        if letra not in string_2:
            resultado += letra
    return resultado
string_01: str = "Hola que tal estas"
string_02: str = "aeiou"

if __name__ == "__main__":
    print(borra_letras(string_01, string_02))