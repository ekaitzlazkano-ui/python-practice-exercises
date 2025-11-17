a_bool: bool = False
b_bool: bool = False
c_bool: bool = False

print("Vamos a jugar a un trivial de 3 preguntas, cuando aciertes pasarás a la próxima pregunta:")

while a_bool == False:
    a = int(input("""
    ¿Cuál es la capital de Francia?
    1) Madrid
    2) Paris
    3) Helsinki
    Responde: """))
    if a == 2:
        a_bool = True
        print("Correcto! Pasas a la pregunta 2.")
    else:
        print("¡No! Inténtalo de nuevo.")
    
while b_bool == False:
    b = int(input("""
    ¿En qué año se descubrió America?
    1) 1789
    2) 1489
    3) 1492
    Responde: """))
    if b == 3:
        b_bool = True
        print("Correcto! Pasas a la pregunta 3.")
    else:
        print("¡No! Inténtalo de nuevo.")

while c_bool == False:
    c = int(input("""
    ¿Cuál es la capital de Polonia?
    1) Varsovia
    2) Praga
    3) Bruselas
    Responde: """))
    if c == 1:
        c_bool = True
        print("Correcto! Te has pasado el juego.")
    else:
        print("¡No! Inténtalo de nuevo.")