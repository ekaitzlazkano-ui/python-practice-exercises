import math

g = float(input("¿Cuál es la gravedad en el planeta en el que estás?"))
velocidad0 = float(input("¿Cuál es la velocidad inicial del salto?"))
ángulo_grados = float(input("¿Cuál es el ángulo de salto?"))
ángulo_radianes = math.radians(ángulo_grados)
seno = math.sin(2*ángulo_radianes)

longitud = (((velocidad0**2)*seno)/g)

print(f"Una persona que salte con un ángulo de {ángulo_grados}° a {velocidad0}m/s  en un planeta con g = {g}m/s^2 recorrería {longitud:.3f}m")