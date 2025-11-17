def menu(operacion: int, valor1:float, valor2:float) -> float:
    resultado: float = 0
    if operacion == 1:
        def sumar(valor1_suma: float, valor2_suma: float) -> float:
            resultado_suma: float = valor1_suma + valor2_suma
            return resultado_suma
        resultado = sumar(valor1, valor2)
    elif operacion == 2:
        def restar(valor1_resta: float, valor2_resta: float) -> float:
            resultado_resta: float = valor1_resta-valor2_resta
            return resultado_resta
        resultado = restar(valor1,valor2)
    elif operacion == 3:
        def multiplicacion(valor1_multiplicacion: float, valor2_multiplicacion: float) -> float:
            resultado_multiplicacion: float = valor1_multiplicacion*valor2_multiplicacion
            return resultado_multiplicacion
        resultado = multiplicacion(valor1,valor2)
    elif operacion == 4:
        def division(valor1_division: float, valor2_division: float) -> float:
            resultado_division: float = valor1_division/valor2_division
            return resultado_division
        resultado = division(valor1,valor2)
    return resultado

operacion_user: int = int(input("""
¿Que operación quieres hacer?
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
Respuesta: """))
valor1_user:float = float(input("Primer valor de la operación: "))
valor2_user:float = float(input("Segundo valor de la operación: "))
resultado_operacion: float = menu(operacion_user, valor1_user, valor2_user)    
print(resultado_operacion)