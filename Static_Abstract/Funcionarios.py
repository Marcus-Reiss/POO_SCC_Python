from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, n, cpf, sb):
        self.nome = n
        self.CPF = cpf
        self.SalarioBase = sb

    @abstractmethod
    def calculaSalario(self):
        pass

    @staticmethod
    def verifica_cpf(cpf):
        soma = 0
        resto = list()

        while True:
            if len(cpf) != 11 or cpf == '00000000000':
                print('Numero de CPF invalido !')
                cpf = str(input('Tente novamente >> ')).strip()
                continue

            # primeiro digito verificador
            for k in range(9):
                soma += int(cpf[k]) * (10 - k)

            resto.append((soma * 10) % 11)
            if resto[0] == 10 or resto[0] == 11:
                resto[0] = 0

            # segundo digito verificador
            soma = 0
            for k in range(10):
                soma += int(cpf[k]) * (11 - k)

            resto.append((soma * 10) % 11)
            if resto[1] == 10 or resto[1] == 11:
                resto[1] = 0

            # verificacao dos restos
            if resto[0] != int(cpf[9]) or resto[1] != int(cpf[10]):
                print('Numero de CPF invalido !')
                cpf = str(input('Tente novamente >> ')).strip()
            else:
                return cpf

class Gerente(Funcionario):

    def __init__(self, n, cpf, sb):
        super().__init__(n, cpf, sb)

    def calculaSalario(self):
        return self.SalarioBase * 2


class Assistente(Funcionario):

    def __init__(self, n, cpf, sb):
        super().__init__(n, cpf, sb)

    def calculaSalario(self):
        return self.SalarioBase


class Vendedor(Funcionario):

    def __init__(self, n, cpf, sb, com):
        super().__init__(n, cpf, sb)
        self.comissao = com

    def calculaSalario(self):
        return self.SalarioBase + self.comissao
