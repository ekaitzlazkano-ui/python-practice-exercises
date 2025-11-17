"""cuenta cuantas veces aparece cada palabra en una frase"""

def cuenta_palabras(texto: str) -> dict[str, int]:
    """cuenta las palabras"""
    texto = texto.lower()
    palabras: list = texto.split(" ")
    resultado: dict = {}
    for palabra in palabras:
        if palabra not in resultado:
            resultado[palabra] = 0
        resultado[palabra] += 1
    return resultado


if __name__ == "__main__":
    print(cuenta_palabras("Hola hola me escuchas que tal me escuchas"))
    