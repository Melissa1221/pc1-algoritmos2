
def karatsuba(x, y):

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    mitad = n // 2

    pow10Mitad = 10 ** mitad
    altoX = x // pow10Mitad
    bajoX = x % pow10Mitad
    altoY = y // pow10Mitad
    bajoY = y % pow10Mitad

    z0 = karatsuba(bajoX, bajoY)
    z2 = karatsuba(altoX, altoY)
    z1 = karatsuba(bajoX + altoX, bajoY + altoY) - z2 - z0

    return (z2 * 10 ** (2 * mitad)) + (z1 * pow10Mitad) + z0

def multiplicacion_fuerza_bruta(x, y):
    strX = str(x)
    strY = str(y)

    n = len(strX)
    m = len(strY)

    resultado = [0] * (n + m)

    for i in range(n - 1, -1, -1):
        acarreo = 0
        for j in range(m - 1, -1, -1):
            prod = int(strX[i]) * int(strY[j]) + acarreo + resultado[i + j + 1]
            resultado[i + j + 1] = prod % 10  
            acarreo = prod // 10 
        resultado[i] += acarreo 

    resultado_str = ''.join(map(str, resultado)).lstrip('0')

    return int(resultado_str) if resultado_str else 0
