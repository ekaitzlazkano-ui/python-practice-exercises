empresa: list = [
    ["Ana", "Dept1", "F", 1500],
    ["Juan", "Dept1", "M", 1500],
    ["Mikel", "Dept2", "M", 1300],
    ["Iñigo", "Dept3", "M", 1700],
    ["Laura", "Dept3", "F", 1650],
    ["Idoia", "Dept4", "F", 1700],
    ["Markel", "Dept5", "M", 1500]
]

promedio_femenino: float = 0
sum_sueldo_fem: int = 0
cantidad_fem: int = 0
superior_1500: int = 0
trabajadores_masculino: list [str] = []

for trabajador in empresa:
    if trabajador[2] == "F":
        cantidad_fem += 1
        sum_sueldo_fem += trabajador[3]
promedio_femenino = sum_sueldo_fem/cantidad_fem
print(f"El sueldo promedio de las mujeres es {promedio_femenino:.2f}€")

for trabajador in empresa:
    if trabajador[3] == 1500:
        superior_1500 += 1

print(f"Hay {superior_1500} trabajadores que cobran más de 1500€")

for trabajador in empresa:
    if trabajador[2] == "M":
        trabajadores_masculino.append(trabajador[0])

print(f"Los trabajadores masculinos son {trabajadores_masculino}")