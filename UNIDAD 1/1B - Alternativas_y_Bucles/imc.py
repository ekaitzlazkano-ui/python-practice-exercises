altura = float(input("¿Cuánto mides en metros?"))
peso = float(input("¿Cuánto pesas en kilogramos?"))

imc: float = peso / (altura**2)
valoracion: str = ""

if imc < 18.5:
    valoracion = "Tu peso es bajo"
elif 18.5 < imc < 25:
    valoracion = "Tu peso es normal"
elif 25 < imc < 30:
    valoracion = "Tienes sobrepeso"
elif 30 < imc:
    valoracion = "Tienes obesidad"

print(f"Pesas: {peso}kg")
print(f"Mides: {altura}m")
print(f"Tu IMC es de {imc:.4f}")
print(valoracion)
