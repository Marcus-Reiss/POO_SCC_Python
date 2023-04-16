# exs 07 e 08
from math import fabs
def line ():
    print('-'*70)

def ab (k):
    if k == 0:
        c = 'a'
    else:
        c = 'b'
    return c

def setCoef ():
    line()
    while True:
        try:
            o = int(input('Ordem da equacao >> '))
            break
        except ValueError:
            print('A ordem deve ser um numero INTEIRO !')

    line()
    coef = list()
    for k in range(o + 1):
        while True:
            try:
                coef.append(float(input(f'Coeficiente que acompanha x^{o - k} >> ')))
                break
            except ValueError:
                print('Digite um numero real !')

    return coef

def f (x, coef):
    f = 0
    for k in range(len(coef)):
        f += coef[k] * x ** (len(coef) - k - 1)
    return f

def df (x, coef):
    df = 0
    for k in range(len(coef)):
        df += coef[k] * (len(coef) - k - 1) * x ** (len(coef) - k - 2)
    return df

def setIntervalo (coef):
    line()
    print('Metodo da bissecao:')

    it = list()
    while True:
        for j in range(2):
            while True:
                try:
                    it.append(float(input(f'Extremo {ab(j)} do intervalo >> ')))
                    break
                except ValueError:
                    print('Digite um numero real !')
        if f(it[0], coef) * f(it[1], coef) < 0:
            break
        else:
            line()
            print('Nao existe raiz no intervalo informado !! Tente novamente !')
            line()
            it.clear()

    while True:
        try:
            erro = float(input('Erro permitido >> '))
            break
        except ValueError:
            print('Digite um numero real !')

    return [it, erro]

def setX0 ():
    line()
    print('Metodo de Newton-Raphson')

    while True:
        try:
            x0 = float(input('Digite o chute inicial >> '))
            break
        except ValueError:
            print('Digite um numero real !')

    while True:
        try:
            erro = float(input('Erro permitido >> '))
            break
        except ValueError:
            print('Digite um numero real !')

    return [x0, erro]

def bissecao (l, coef):
    a = l[0][0]
    b = l[0][1]
    erro = l[1]
    err = 2 * erro
    xkm1 = 0
    iteracoes = 0

    while err > erro:
        iteracoes += 1
        xk = (a + b)/2
        if f(a, coef) * f(xk, coef) < 0:
            b = xk
        elif f(xk, coef) * f(b, coef) < 0:
            a = xk
        xkm1 = (a + b)/2
        err = fabs(xkm1 - xk) / fabs(xkm1)

    return [xkm1, iteracoes]

def newtonRaphson (l, coef):
    x0 = l[0]
    erro = l[1]
    err = 2 * erro
    xkm1 = 0
    iteracoes = 0

    while err > erro:
        iteracoes += 1
        xkm1 = x0 - f(x0, coef) / df(x0, coef)
        err = fabs(xkm1 - x0) / fabs(xkm1)
        x0 = xkm1

    return [xkm1, iteracoes]

def printRaiz (ri):
    line()
    print(f'A raiz encontrada foi {ri[0]}')
    print(f'Foram usadas {ri[1]} iteracoes')
    line()

def menu (coef):
    while True:
        line()
        print('Escolha um dos metodos:')
        print('[1] Bissecao' + ' ' * 30 + '[2] Newton-Raphson')
        while True:
            try:
                resposta = int(input('Escolha (0 para sair) >> '))
                if resposta != 1 and resposta != 2 and resposta != 0:
                    print('Digite 1 ou 2 !!')
                    continue
                break
            except ValueError:
                print('Digite 1 ou 2 !!')
        if resposta == 0:
            return
        analisaResposta(resposta, coef)

def analisaResposta (resposta, coef):
    if resposta == 1:
        l = setIntervalo(coef)
        ri = bissecao(l, coef)
    else:
        l = setX0()
        ri = newtonRaphson(l, coef)

    printRaiz(ri)

coef = setCoef()
menu(coef)
