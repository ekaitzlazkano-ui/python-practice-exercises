asignaturas: list [str] = ["programación", "cálculo", "álgebra", "electrónica digital", "introducción a los computadores"]
calificaciones: list [int] = []
suma: int = 0
for asignatura in asignaturas:
    calificaciones.append(int(input(f"Introduce tu calificación de {asignatura}: ")))
for calificacion in calificaciones:
    suma += calificacion
media: float = suma/len(asignaturas)
print(f"Calificación media: {media}")