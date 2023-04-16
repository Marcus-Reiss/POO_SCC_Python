# ex 06
def setFloat ():
    n = list()
    while True:
        try:
            k = float(input('Digite um numero real (0 para sair) >> '))
            n.append(k)
            if k == 0:
                break
        except ValueError:
            print('ERRO !! Tente novamente !')
    return n

def menorMaior (n):
    menor = maior = n[0]
    for k in n:
        if menor > k:
            menor = k
        elif maior < k:
            maior = k
    return [menor, maior]

def conclui (l):
    print(f'Menor dos valores digitados: {l[0]}')
    print(f'Maior dos valores digitados: {l[1]}')

n = setFloat()
l = menorMaior(n)
conclui(l)
