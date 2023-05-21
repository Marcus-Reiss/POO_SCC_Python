class Premio:
    def __init__(self):
        self.creditos = 200

    def get_score(self, aposta, cartas):
        scorep = list()
        for i in range(8):
            scorep.append(False)
        score = 0

        cartas_num = [x % 13 for x in cartas]
        cartas_naipe = list()
        for x in cartas:
            if x < 13:
                cartas_naipe.append(0)
            elif x < 26:
                cartas_naipe.append(1)
            elif x < 39:
                cartas_naipe.append(2)
            else:
                cartas_naipe.append(3)

        set_num   = set(cartas_num)
        set_naipe = set(cartas_naipe)

        # 0 - DUPLA
        if len(set_num) == 3:
            for elem in cartas:
                if cartas.count(elem) == 2:
                    scorep[0] = True

        # 1 - TRINCA
