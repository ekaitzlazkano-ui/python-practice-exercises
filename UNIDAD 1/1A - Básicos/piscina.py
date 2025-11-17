ancho = float(input("¿Cuántos metros de ancho tiene tu piscina?"))
largo = float(input("¿Cuántos metros de largo tiene tu piscina?"))
profundidad = float(input("¿Cuántos metros de profundidad tiene tu piscina?"))
volumen:float = ancho*largo*profundidad
litros:float = volumen*1000
print("Una piscina de", ancho, "metros de ancho,", largo, "m de largo y", profundidad, "m de profundidad contiene", litros, "litros de agua")