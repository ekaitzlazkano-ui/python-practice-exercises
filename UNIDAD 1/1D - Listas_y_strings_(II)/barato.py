import math
precios: list[float] = [123.50, 23.0, 12.99, 11.50, 67.40, 44.35, 111.0, 19.0, 75.5, 99.99]
barato: float = math.inf
for precio in precios:
    if precio<barato:
        barato = precio
print(f"El precio más barato es {barato}")