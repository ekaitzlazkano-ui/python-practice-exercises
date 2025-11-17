numeros:list[int] = list(range(1,101))
numero:int = int(input(f"Dime un número entre {numeros[0]} y {numeros[-1]}: "))
inferior: int = 0
superior: int = len(numeros) - 1
mitad  = (superior - inferior) // 2
while numeros[mitad] != numero:
    if numeros[mitad] > numero:
        print(f"({inferior+1} - {superior+1}) Está en la posición {mitad+1}? No, es menor ")
        superior = mitad
    else:
        print(f"({inferior+1} - {superior+1}) Está en la posición {mitad+1}? No, es mayor ")
        inferior = mitad
    mitad = inferior + (superior-inferior) // 2
print(f"({inferior+1} - {superior+1}) Está en la posición {mitad+1}? Sí")