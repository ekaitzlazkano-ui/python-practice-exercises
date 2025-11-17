altura = float(input("¿Cuántos metros de alto tiene tu pared?"))
anchura = float(input("¿Cuántos metros de ancho tiene tu pared?"))
ventanas = int(input("¿Cuántas ventanas tiene la pared?"))
puertas = int(input("¿Cuántas puertas tiene la pared?"))
decimales_litros = 2

superficie: float = (altura*anchura)-((ventanas*1)+(puertas*1.6))
litros: float = superficie / 10
#f-string, todo como texto y las variables entre corchetes. Puedo definir los decimales de la variable -->{variable:.nf} siendo n el número de decimales
print(f"Una pared de {altura} m de alto y {anchura} m de ancho con {ventanas} ventana(s) y {puertas} puerta(s) necesita {litros:.{decimales_litros}f} litros de pintura")