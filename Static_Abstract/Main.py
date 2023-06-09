from Funcionarios import *

class Main:

    def __init__(self):
        self.funcsG = list()
        self.funcsA = list()
        self.funcsV = list()

    def le_opcao(self):
        print("""
++++++++++++++++++++++++++++++++++++++++++++++
[1] Cadastrar um Gerente
[2] Cadastrar um Assistente
[3] Cadastrar um Vendedor
[4] Exibir folha salarial dos funcionarios
[5] Sair
++++++++++++++++++++++++++++++++++++++++++++++""")
        while True:
            k = int(input('Opcao desejada >> '))
            if 0 < k < 6:
                return k

    def print_folha(self):
        folha = 0

        for g in self.funcsG:
            print(f'Nome do gerente: {g.nome}')
            print(f'CPF do gerente: {m.formata_cpf(g.CPF)}')
            print(f'Salario: {g.calculaSalario()}')
            print()
            folha += g.calculaSalario()

        for a in self.funcsA:
            print(f'Nome do assistente: {a.nome}')
            print(f'CPF do assistente: {m.formata_cpf(a.CPF)}')
            print(f'Salario: {a.calculaSalario()}')
            print()
            folha += a.calculaSalario()

        for v in self.funcsV:
            print(f'Nome do vendedor: {v.nome}')
            print(f'CPF do vendedor: {m.formata_cpf(v.CPF)}')
            print(f'Salario: {v.calculaSalario()}')
            print()
            folha += v.calculaSalario()

        print('Folha salarial dos funcionarios:')
        print(f'Valor total = {folha}')

    def formata_cpf(self, cpf):
        return cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]


if __name__ == '__main__':
    op = 0
    m = Main()

    sb = float(input('Definir salario base >> '))

    while True:
        op = m.le_opcao()
        if op == 1:
            print('\nOPCAO 1 [Cadastro de Gerente]:')
            n = str(input('Nome do gerente >> ')).strip()
            cpf0 = str(input('CPF do gerente >> ')).strip()
            cpf = Funcionario.verifica_cpf(cpf0)
            g = Gerente(n, cpf, sb)
            m.funcsG.append(g)
            print('[------------ Gerente cadastrado -------------]')
        elif op == 2:
            print('\nOPCAO 2 [Cadastro de Assistente]:')
            n = str(input('Nome do assistente >> ')).strip()
            cpf0 = str(input('CPF do assistente >> ')).strip()
            cpf = Funcionario.verifica_cpf(cpf0)
            a = Assistente(n, cpf, sb)
            m.funcsA.append(a)
            print('[------------ Assistente cadastrado -------------]')
        elif op == 3:
            print('\nOPCAO 3 [Cadastro de Vendedor]:')
            n = str(input('Nome do vendedor >> ')).strip()
            cpf0 = str(input('CPF do vendedor >> ')).strip()
            cpf = Funcionario.verifica_cpf(cpf0)
            com = float(input('Comissao >> '))
            v = Vendedor(n, cpf, sb, com)
            m.funcsV.append(v)
            print('[------------ Vendedor cadastrado -------------]')
        elif op == 4:
            print('\nOPCAO 4 [Impressao - Folha salarial]:')
            m.print_folha()
        elif op == 5:
            print('\nFinalizando o programa...')
            break
