import math

a = float(input("¿Cuántos metros mide el lado a del triángulo?"))
b = float(input("¿Cuántos metros mide el lado b del triángulo?"))
c = float(input("¿Cuántos metros mide el lado c del triángulo?"))

s: float = (a+b+c)/2

área = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f"Un triángulo con lados de {a}, {b} y {c} tiene {área:.3f} m2.")