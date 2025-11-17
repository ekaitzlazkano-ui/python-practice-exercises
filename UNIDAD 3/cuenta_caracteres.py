"""contador de cada caracter en el texto"""

def contar_caracteres(texto: str) -> dict[str, int]:
    """cuenta el cuantas veces se encuentra cada caracter en el texto"""
    resultado: dict = {}
    for letra in texto:
        if letra not in resultado:
            resultado[letra] = 0
        resultado[letra] += 1
    return resultado


if __name__ == "__main__":
    print(contar_caracteres("abcd 11 abbb ?"))
