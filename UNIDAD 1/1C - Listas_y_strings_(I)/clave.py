import random
import string
alphabet: list = list(string.ascii_lowercase)
password: str = ""
digits: int = int(input("De cuántos dígitos quieres que sea la clave? "))
for i in range(1,digits+1,1):
    password += alphabet[random.randint(0,len(alphabet)-1)]
print(f"La clave es {password}")