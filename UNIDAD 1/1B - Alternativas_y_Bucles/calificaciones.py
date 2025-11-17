nota = float(input("¿Qué nota has sacado?"))
calificación: str = ""

if 0<= nota < 5:
    calificación = "SUSPENSO"
elif nota < 6:
    calificación = "SUFICIENTE"
elif nota < 7:
    calificación = "BIEN"
elif nota < 9:
    calificación = "NOTABLE"
elif nota <= 10:
    calificación = "SOBRESALIENTE"
else:
    print("Las notas tienen que ser de 0 a 10")

print(f"""
Nota: {nota}
Calificación: {calificación}
""")