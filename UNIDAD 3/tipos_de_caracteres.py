ALPHABET: str = "abcdefghijklmnñopqrstuvwxyz"
NUMBERS: str = "0123456789"

def tipos_de_caracteres(text: str) -> list:
    result: list = []
    text = text.lower()
    for letter in text:
        if letter in ALPHABET:
            result.append(1)
        elif letter in NUMBERS:
            result.append(2)
        else:
            result.append(0)
    return result


if __name__ == "__main__":
    print(tipos_de_caracteres("abcd 12 ABC"))
