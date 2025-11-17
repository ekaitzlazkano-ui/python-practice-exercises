coste = float(input("¿Cuánto te ha costado la compra?"))
pagado = float(input("¿Cuánto has pagado?"))

print(coste)
print(pagado)
devolver = pagado - coste
print(devolver)

monedas2 = devolver // 2        #cantidad monedas 2 euros
devolver = devolver - (monedas2 * 2)
monedas1 = devolver // 1        #cantidad monedas 1 euro
devolver = devolver - (monedas1 * 1)
monedas050 = devolver // 0.5    #cantidad monedas 50 cents.
devolver = devolver - (monedas050 * 0.5)
monedas020 = devolver // 0.2    #cantidad monedas 20 cents.
devolver = devolver - (monedas020 * 0.2)
monedas010 = devolver // 0.1    #cantidad monedas 10 cents.
devolver = devolver - (monedas010 * 0.1)
monedas005 = devolver // 0.05   #cantidad monedas 5 cents.
devolver = devolver - (monedas005 * 0.05)
monedas002 = devolver // 0.02   #cantidad monedas 2 cents.
devolver = devolver - (monedas002 * 0.01)
monedas001 = devolver // 0.01   #cantidad monedas 1 cents.

print(f"""
{monedas2:.0f} monedas de 2€
{monedas1:.0f} monedas de 1€
{monedas050:.0f} monedas de 50 c
{monedas020:.0f} monedas de 20 c
{monedas010:.0f} monedas de 10 c
{monedas005:.0f} monedas de 5 c
{monedas002:.0f} monedas de 2 c
{monedas001:.0f} monedas de 1 c
""")
#se podría solucionar el problema de los decimales pasando al principio del programa a centimos
#el precio entonces no habría decimales y se podría hacer el programa en centimos