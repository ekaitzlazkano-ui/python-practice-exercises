aprobados: list[str] = ["Ekaitz", "Iker", "Ander", "Unai", "Jon"]

nombre = str(input("Dime un nombre y te dire si ha aprobado"))
nombre = nombre.lower()
nombre = nombre.capitalize()

if nombre in aprobados:
    print(f"{nombre} sí está en la lista de aprobados")
else:
    print(f"{nombre} no está en la lista de aprobados")