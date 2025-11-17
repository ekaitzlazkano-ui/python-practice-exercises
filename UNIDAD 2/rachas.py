def calcular_rachas(numeros: list [int])-> int:
    numeros_racha: list [int] =[]
    racha: int = 0
    for i in range(len(numeros)-1):
        if numeros[i] == numeros[i+1]:
            if numeros[i] not in numeros_racha:
                numeros_racha.append(numeros[i])
                racha+=1
    return racha
numeros_inicio: list [int] = [1,2,3,3,3,2,2,4]
print(calcular_rachas(numeros_inicio))