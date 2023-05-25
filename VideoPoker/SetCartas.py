from Carta import Carta
from time import sleep

class SetCartas:
    def __init__(self, n_cartas=5):
        self.n_cartas = n_cartas
        self.cartas = list()
        for k in range(n_cartas):
            self.cartas.append(Carta())
            sleep(0.001)  # evitar interpretacao equivocada do unix_time_millis (classe Random)

    mao = list()  # armazena uma carta em cada posicao

    def set_mao(self, s='', ja_foi=False):
        if s.strip() == '' and not ja_foi:
            for k in range(self.n_cartas):
                self.mao.append(self.cartas[k].set_carta())
        elif s.strip() != '' and ja_foi:
            trocar = s.strip().split()
            for k in range(len(trocar)):
                self.mao[int(trocar[k]) - 1] = self.cartas[int(trocar[k]) - 1].set_carta()

        return self.mao

    def __str__(self):
        string_array = list()
        for k in range(self.n_cartas):
            string_array.append(str(self.cartas[k]))

        div = list()
        for string in string_array:
            div.append(string.split('\n'))

        joined = list()
        for j in range(len(div[0])):
            joined.append('')

        for j in range(len(div[0])):
            for k in range(self.n_cartas):
                joined[j] += div[k][j] + '   '

        string_final = '  (1)        (2)        (3)        (4)        (5)\n'
        for string in joined:
            string_final += string + '\n'

        return string_final
