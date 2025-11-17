import math
valores: list[int] = []
for i in range(10):
    a = (int(input(f"Dime la {i+1} altura: ")))
    valores.append(a)
sumatorio: int = 0
for valor in valores:
    sumatorio += valor
media: float = sumatorio/len(valores)
print(f"La medía de los números es {media}")

sumatorio_desv: float = 0
for valor in valores:
    sumatorio_desv += (valor-media)**2
desv_tipica = math.sqrt(sumatorio_desv / (len(valores)-1))
print(f"Desv. típica: {desv_tipica:.3f}")

minimo: float = math.inf
for valor in valores:
    if valor < minimo:
        minimo = valor
print(f"Áltura mínima: {minimo}")

maximo: int = 0
for valor in valores:
    if valor > maximo:
        maximo = valor
print(f"Áltura máxima: {maximo}")