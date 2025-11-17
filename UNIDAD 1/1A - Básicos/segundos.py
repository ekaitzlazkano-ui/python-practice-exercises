segundos1 = int(input("Dime una cantidad de segundos y te lo daré en horas, minutos y segundos"))

horas = segundos1 // (60*60)             #calcúlo horas
segundos2 = segundos1 - (horas *60*60)   #segundos restantes tras restar horas

minutos = segundos2 // 60                #calcúlo minutos
segundos3 = segundos2 - (minutos*60)     #segundos restantes tras restar minutos

print(f"{segundos1}segundos son {horas}horas, {minutos}minutos y {segundos3} segundos")