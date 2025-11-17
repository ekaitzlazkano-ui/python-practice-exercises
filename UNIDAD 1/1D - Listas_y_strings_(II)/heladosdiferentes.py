sabores: list [str] = ["Chocolate", "Vainilla", "Fresa", "Nata", "Limón"]
for sabor1 in sabores:
    for sabor2 in sabores:
        if sabor2 != sabor1:
            for sabor3 in sabores:
                if sabor3 != sabor2 and sabor3 != sabor1:
                    print(sabor1, sabor2, sabor3)
