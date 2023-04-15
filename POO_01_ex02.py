# ex02 - eq do 2o grau
from math import sqrt

def abc (n):
    if n == 0:
        c = 'a'
    elif n == 1:
        c = 'b'
    else:
        c = 'c'
    return c

def setCoef ():
    coef = list()
    for k in range(3):
        while True:
            try:
                coef.append(float(input(f'Digite o coeficiente {abc(k)} >> ')))
                break
            except ValueError:
                print('ERRO !! Digite um numero real !')
    print(coef)
    return coef

def baskhara (coef):
    a = coef[0]
    b = coef[1]
    c = coef[2]
    raiz = list()
    delta = b**2 - 4*a*c
    if delta < 0:
        print('A eq nao possui raiz real !')
    else:
        raiz.append((-b + sqrt(delta))/(2*a))
        raiz.append((-b - sqrt(delta))/(2*a))
        printRaiz(raiz)

def printRaiz (raiz):
    print('As raizes da equacao sao:')
    print(f'x1 = {raiz[0]}')
    print(f'x2 = {raiz[1]}')

coef = setCoef()
baskhara(coef)
