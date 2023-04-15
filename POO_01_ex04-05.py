# exs 04 e 05
# considerando o conjunto dos naturais
def setInt ():
    while True:
        try:
            n = int(input('Digite um inteiro >> '))
            break
        except ValueError:
            print('ERRO !! Digite um INTEIRO !')
    return n

def verificaPrimo (n):
    if n == 0 or n == 1:
        b = False
    else:
        c = 0
        for k in range(1, n // 2 + 1):
            if n % k == 0:
                c += 1
        b = False if c > 1 else True
    return b

def menorDivisor (n):
    md = 0
    for k in range(2, n):
        if n % k == 0:
            md = k
            break
    return md

def primeiroPrimo (n):
    pp = 0
    for k in range(n - 1, 1, -1):
        if verificaPrimo(k):
            pp = k
            break
    return pp

def conclui (n):
    if verificaPrimo(n):
        print(f'O numero {n} eh primo !')
    else:
        print(f'O numero {n} NAO eh primo !')
        print(f'O menor divisor de {n} eh {menorDivisor(n)}')
    print(f'O primeiro primo menor que {n} eh {primeiroPrimo(n)}')

n = setInt()
conclui(n)
