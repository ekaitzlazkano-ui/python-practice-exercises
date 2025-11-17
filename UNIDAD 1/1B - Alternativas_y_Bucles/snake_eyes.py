import random
i:int = 0
n:int = 0
dado1:int = 0
dado2:int = 0

while i == 0:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    n = n +1
    if dado1 == 1 and dado2 == 1:
        break

print(f"Has tenido que tirar los dados {n} veces para que te salga un ojos de serpiente")