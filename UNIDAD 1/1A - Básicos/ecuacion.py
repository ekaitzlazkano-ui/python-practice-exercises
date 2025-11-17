import math

a = float(input("¿Cuál es el valor de a en la ecuación de segundo grado?"))
b = float(input("¿Cuál es el valor de b en la ecuación de segundo grado?"))
c = float(input("¿Cuál es el valor de c en la ecuación de segundo grado?"))

d = b**2 - 4*a*c

if d >= 0:
    x1 = (-b + math.sqrt(d))/2*a
    x2 = (-b - math.sqrt(d))/2*a
    if x1 == x2:
        print(f"La solución de la ecuación es x={x1:.3f}")
    else:
        print(f"Las soluciones de la ecuación son x={x1:.3f} y x={x2:.3f}")
