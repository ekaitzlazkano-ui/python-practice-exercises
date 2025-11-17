ALPHABET: str = "abcdefghijklmnñopqrstuvwxyz"

def letters(text: str) -> list:
    result: list = []
    text = text.lower()
    for letter in text:
        if letter in ALPHABET:
            result.append(1)
        else:
            result.append(0)
    return result


if __name__ == "__main__":
    print(letters("abcd 12 ABC"))