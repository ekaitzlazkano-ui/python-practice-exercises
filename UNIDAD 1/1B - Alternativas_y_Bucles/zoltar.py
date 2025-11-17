nombre = str(input("¿Cómo te llamas?"))
nombre = nombre.capitalize()
primer_apartado: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H"]
segundo_apartado: list[str] = ["I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q"]
tercer_apartado: list[str] = ["R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

if nombre[0] in primer_apartado:
    print(f"{nombre}, te auguro un futuro con éxito")
elif nombre[0] in segundo_apartado:
    print(f"{nombre}, te auguro un futuro con mucho dinero")
elif nombre[0] in tercer_apartado:
    print(f"{nombre}, te auguro un futuro con muchas dificultades")
else:
    print("Lo siento, tu nombre tiene que empezar por una letra de la A a la Z")
