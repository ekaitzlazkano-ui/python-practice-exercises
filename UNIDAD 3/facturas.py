import math

def calc_total(dict_facturas: dict)->float:
    """devuelve valor total de facturas"""
    total: float = 0
    for factura in dict_facturas:
        total += dict_facturas[factura]
    return total

def mayor_factura(dict_facturas: dict)->str:
    """devuelve factura mas alta"""
    mayor: float = -math.inf
    resultado: str = ""
    for factura in dict_facturas:
        if dict_facturas[factura] > mayor:
            mayor = dict_facturas[factura]
            resultado = factura
    return resultado

if __name__ == "__main__":
    dict_facturas = {
    "F190374": 140.00,
    "F190370": 75.47,
    "F190271": 99.99,
    "F190057": 1050.25,
    }
    print(calc_total(dict_facturas))
    print(mayor_factura(dict_facturas))