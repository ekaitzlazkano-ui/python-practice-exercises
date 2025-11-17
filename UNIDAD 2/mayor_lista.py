def es_lista_mayor(numeros_1: list, numeros_2: list) -> bool:
    if len(numeros_1) == len(numeros_2):
        solucion: bool = True
        for i in range(len(numeros_1)):
            if numeros_1[i] <= numeros_2[i]:
                solucion = False    
        return solucion
    else:
        print("Las listas no tienen la misma longitud")
        """Añado esta última línea porque si no vsc me marca en rojo el "-> bool" por no haber return en esta parte del if,
        pero no sé como podría hacerlo para que no me lo marque en rojo y que si pasa "else" no haya return porque no quiero
        que aparezca en consola el False despues del mensaje de "Las listas no tienen la misma longitud", yo usaría un exit() :)"""
        return False

lista1: list [int] = [1,3,5]
lista2: list [int] = [0,2,4]
resultado: bool = es_lista_mayor(lista1, lista2)
print(resultado)