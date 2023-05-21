from Random import Random

class Carta:

    def __init__(self):
        rd = Random()
        self.rd = rd


    carta = 0

    def set_carta(self):
        self.carta = self.rd.get_int_rand(52)
        return self.carta

    def __str__(self):
        # codificacao
            # naipes (unicode): \u2660 (espadas); \u2663 (paus); \u2665 (copas); \u2666 (ouros)
            # espadas: 0 a 12; paus: 13 a 25; copas: 26 a 38; ouros: 39 a 51

        cod_num   = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        cod_naipe = ['\u2660', '\u2663', '\u2665', '\u2666']

        decod_num = decod_naipe = ''

        for pos, valor in enumerate(cod_num):
            if self.carta % 13 == pos:
                decod_num = valor
                break

        if self.carta < 13:
            decod_naipe = cod_naipe[0]
        elif self.carta < 26:
            decod_naipe = cod_naipe[1]
        elif self.carta < 39:
            decod_naipe = cod_naipe[2]
        else:
            decod_naipe = cod_naipe[3]

        s = f"""+------+\n|      |\n| {decod_num:2} {decod_naipe} |\n|      |\n+------+"""

        return s
