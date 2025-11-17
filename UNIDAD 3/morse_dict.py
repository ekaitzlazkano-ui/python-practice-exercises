"""pasa de texto a morse"""

MORSE: dict = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--.."
}


def codificador(texto: str, diccionario: dict):
    """convertidor de texto a morse"""
    resultado: str = ""
    texto = texto.lower()
    for letra in texto:
        if letra in diccionario:
            resultado += diccionario[letra]
        else:
            resultado += letra
        resultado += " "
    return resultado


if __name__ == "__main__":
    print(codificador("hola que tal estas", MORSE))
