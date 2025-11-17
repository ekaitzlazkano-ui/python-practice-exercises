t: int = 0 
v: float = 9.8 * t
s: float = 1/2 * 9.8 * t**2

while t<= 10:
    print(f"t = {t}s, v = {v:.2f}m/s, {s:.2f} metros recorridos.")
    t = t+1
    v = 9.8*t
    s = 1/2 * 9.8 * t**2