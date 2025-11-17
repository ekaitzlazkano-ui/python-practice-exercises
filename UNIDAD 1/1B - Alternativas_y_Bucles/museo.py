dia_bool = bool(input("¿Es miércoles?(si no es, no respondas nada)"))
edad: int = 0

if dia_bool:
    print("¡Los miércoles la entrada es gratis para todo el mundo!")
else:
    edad = int(input("¿Cuántos años tienes?"))
    if edad < 5:
        print("Enhorabuena, entras gratis por tener menos de 5 años.")
    elif edad <= 18:
        print("Tienes tarifa joven y solo pagas 5€")
    elif edad < 64:
        print("Pagas tarifa de adulto, de 10€")
    elif edad > 65:
        print("Tienes una tarifa reducida por ser jubilado, pagas 7€")