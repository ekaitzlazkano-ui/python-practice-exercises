import random
password: str = ""
digits: int = int(input("De cuántos dígitos quieres que sea la clave? "))
for i in range(1,digits+1,1):
    password += str(random.randint(0,9))
print(f"La clave es {password}")