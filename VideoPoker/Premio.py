class Premio:
    def __init__(self, creditos=200):
        self.creditos = creditos

    def get_score(self, aposta, cartas):
        self.creditos -= aposta

        scorep = list()
        for i in range(8):
            scorep.append(0)
        score = 0

        cartas_num = [x % 13 for x in cartas]
        cartas_naipe = list()
        for x in cartas:
            if x < 13:
                cartas_naipe.append(0)  # espadas
            elif x < 26:
                cartas_naipe.append(1)  # paus
            elif x < 39:
                cartas_naipe.append(2)  # copas
            else:
                cartas_naipe.append(3)  # ouros

        set_num   = list(set(cartas_num))
        set_naipe = list(set(cartas_naipe))

        # 0 - DUPLA
        if len(set_num) == 3:
            for elem in cartas_num:
                if cartas_num.count(elem) == 2:
                    scorep[0] = 1
                    print('Parabens ! Voce obteve uma DUPLA !')
                    break

        # 1 - TRINCA
        if len(set_num) == 3:
            for elem in cartas_num:
                if cartas_num.count(elem) == 3:
                    scorep[1] = 1
                    print('Parabens ! Voce obteve uma TRINCA !')
                    break

        # 2 - STRAIGHT (5 CARTAS SEGUIDAS DE NAIPES DIFERENTES)
        if len(set_num) == 5 and len(set_naipe) > 1:
            cont = 0
            for i in range(4):
                if (set_num[i + 1] - set_num[i]) == 1:
                    cont += 1
            if cont == 4:
                scorep[2] = 1
                print('Parabens ! Voce obteve um STRAIGHT !')

        # 3 - FLUSH (5 CARTAS DO MESMO NAIPE NAO SEGUIDAS)
        # 4 - STRAIGHT FLUSH (5 CARTAS SEGUIDAS DO MESMO NAIPE)
        # 5 - ROYAL STRAIGHT FLUSH (5 CARTAS SEGUIDAS DO MESMO NAIPE DE 10 A As)
        if len(set_naipe) == 1:
            if (len(set_num) == 5):
                cont = 0
                for i in range(4):
                    if (set_num[i + 1] - set_num[i]) == 1:
                        cont += 1
                if cont == 4:
                    if set_num[0] == 8:  # 8 corresponde ao n 10
                        scorep[5] = 1
                        print('Parabens ! Voce obteve um ROYAL STRAIGHT FLUSH !')
                    else:
                        scorep[4] = 1
                        print('Parabens ! Voce obteve um STRAIGHT FLUSH !')
                    # scorep[4] = True
                else:
                    scorep[3] = 1
                    print('Parabens ! Voce obteve um FLUSH !')
            else:
                scorep[3] = 1
                print('Parabens ! Voce obteve um FLUSH !')

        # 6 - FULL HAND (UMA TRINCA E UM PAR)
        if len(set_num) == 1:
            scorep[6] = 1
            print('Parabens ! Voce obteve um FULL HAND !')
        elif len(set_num) == 2:
            n = list()
            for i in cartas_num:
                n.append(cartas_num.count(i))
            parabens = int(list(set(n)) == [2, 3])
            scorep[6] = parabens
            if parabens:
                print('Parabens ! Voce obteve um FULL HAND !')

        # 7 - QUADRA
        if len(set_num) == 2:
            n = list()
            for i in cartas_num:
                n.append(cartas_num.count(i))
            parabens = int(list(set(n)) == [1, 4])
            scorep[7] = parabens
            if parabens:
                print('Parabens ! Voce obteve uma QUADRA !')

        # SCORE
        score_cod = [1, 2, 5, 10, 100, 200, 20, 50]
        for i in range(8):
            score += scorep[i] * score_cod[i]

        premio = aposta * score
        if premio == 0:
            print('Que pena! Voce nao ganhou nada essa rodada...')
        self.creditos += premio

        return self.creditos
