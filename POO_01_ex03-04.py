# exs 03 e 04
def setN ():
    while True:
        try:
            n = int(input('Digite um inteiro >> '))
            break
        except ValueError:
            print('ERRO !! Digite um INTEIRO !')
    return n

def trees (n):
    b = setB()
    if b:
        for k in range(n, 0, -1):
            for j in range(k):
                print('*', end='')
            print()
    else:
        for k in range(n):
            for i in range(k):
                print(' ', end='')
            for j in range(n - k):
                print('*', end='')
            print()

def setB ():
    while True:
        try:
            print('Escolha uma opcao:')
            print('[1] Arvore 1' + ' '*10 + '[2] Arvore 2')
            escolha = int(input('>> '))
            break
        except ValueError:
            print('ERRO !! Digite 1 ou 2 !')
    b = True if escolha == 1 else False
    return b

n = setN()
trees(n)
