# Exercicios POO (ex. 02 - classe Adivinha)
class Adivinha:
    def __init__(self):
        self.n0 = 0
        self.bo = False
        self.j = 0
        self.n = self.setInteiro()

    def adivinha (self):
        while True:
            self.j = int ((self.n + self.n0) / 2)
            resposta = self.questiona()
            self.analisaResposta(resposta)
            if self.bo:
                break

    def questiona (self):
        print('-'*60)
        print(f'O numero que voce pensou eh maior, menor ou igual a {self.j} ?')
        print('[1] MAIOR' + ' '*12 + '[2] MENOR' + ' '*12 + '[3] IGUAL')
        resposta = self.setInteiro(q=1)
        return resposta

    def analisaResposta (self, resposta):
        if resposta == 1:
            self.n0 = int ((self.n + self.n0) / 2) + 1
        elif resposta == 2:
            self.n = self.j
        elif resposta == 3:
            print('*'*60)
            print(f'Legal !! O numero que voce pensou foi {self.j}')
            self.bo = True

    def setInteiro (self, q = None):
        if not q:
            while True:
                try:
                    n = int(input('Digite o extremo superior do intervalo >> '))
                    break
                except ValueError:
                    print('Tente novamente ! Digite um INTEIRO !')
        else:
            while True:
                try:
                    n = int(input('Escolha 1, 2 ou 3 >> '))
                    if n not in [1, 2, 3]:
                        print('Erro ! Digite uma das opcoes listadas !')
                    else:
                        break
                except ValueError:
                    print('Erro !! Tente novamente !')
        return n

if __name__ == '__main__':
    obj = Adivinha()
    obj.adivinha()
