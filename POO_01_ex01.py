# ex 001 - raiz quadrada
from math import fabs


def setValues():
    while True:
        try:
            x = float(input("Numero cuja raiz deseja obter >> "))
            break
        except ValueError:
            print("ERRO !! Digite um numero real !")

    while True:
        try:
            x0 = float(input("Chute inicial >> "))
            break
        except ValueError:
            print("ERRO !! Digite um numero real !")

    while True:
        try:
            erro = float(input("Erro permitido >> "))
            break
        except ValueError:
            print("ERRO !! Digite um numero real !")

    values = [x, x0, erro]
    return values


def raiz(values):
    x = values[0]
    x0 = values[1]
    erro = values[2]
    err = 2 * erro
    while err > erro:
        xkm1 = (x0 + x / x0) / 2
        err = fabs(xkm1 - x0)
        x0 = xkm1

    return x0


def printRaiz(x, raiz):
    print(f'Raiz de {x} : sqrt({x}) = {raiz:.10}')


values = setValues()
raiz = raiz(values)
printRaiz(values[0], raiz)
