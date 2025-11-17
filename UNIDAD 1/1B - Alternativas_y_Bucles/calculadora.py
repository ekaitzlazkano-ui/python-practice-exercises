operación = int(input("""
Opciones:
1. Sumar        3. Multiplicar
2. Restar       4. Dividir
Responde aqui --> """))
print(f"Opción elegida: {operación}")

a = float(input("¿Cuál es el primer operando?"))
b = float(input("¿Cuál es el segundo operando?"))

if operación == 1:
    c = a+b
    print(f"{a} + {b} = {c}")
elif operación == 2:
    c = a-b
    print(f"{a} - {b} = {c}")
elif operación == 3:
    c = a*b
    print(f"{a} * {b} = {c}")
elif operación == 4:
    c = a/b
    print(f"{a}/{b} = {c}")