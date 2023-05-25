# Video Poker (main)

from SetCartas import SetCartas
from Premio import Premio

sc = SetCartas()

creditos = 200
rodada = 0

print('-'*25 + ' Video Poker ' + '-'*25)

while True:
    rod = str(input('Digite ENTER para iniciar a rodada (ou s para terminar) >> ')).strip()
    if rod == 's':
        print('Obrigado por jogar o video poker !')
        break
    rodada += 1

    print(f'\nRODADA [{rodada}] ' + '*'*52)

    pr = Premio(creditos)

    while True:
        aposta = int(input('Aposta >> '))
        if creditos >= aposta > 0:
            break
        print('Aposta maior que o numero de creditos ! Digite outro valor !')
    print('-'*63)

    cartas = sc.set_mao()
    print(sc)

    for i in range(2):
        s = str(input('Cartas que deseja trocar >> '))
        cartas = sc.set_mao(s, True)
        print(sc)

    creditos = pr.get_score(aposta, cartas)
    print(f'Creditos: {creditos}')
    print('-'*63)

    cartas.clear()

    if creditos == 0:
        print('Que pena ! Voce perdeu todos os creditos...')
        print('Obrigado por jogar o video poker !')
        break
