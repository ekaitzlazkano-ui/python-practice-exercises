i = 0

nombres:list[str] = ["Ekaitz", "Iker", "Jon", "Diego"]

while i == 0:
    usuario:str = str(input("Dime un nombre: "))
    usuario = usuario.lower()
    usuario_check = usuario.capitalize()
    if usuario == "salir":
        break
    else:
        if usuario_check in nombres:
            print(f"Conozco a {usuario}")
        else:
            nombres.append(usuario_check)
            print(f"No conocía a {usuario}, ahora ya sí")
    
