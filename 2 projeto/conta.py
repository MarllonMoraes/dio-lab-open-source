# conta.py

class Conta:
    proximo_numero = 1

    def __init__(self, titular, cpf, senha):
        self.numero = Conta.proximo_numero
        Conta.proximo_numero += 1
        self.titular = titular
        self.cpf = cpf
        self.senha = senha
        self.saldo = 0
        self.extrato = []

    def obter_saldo(self):
        return self.saldo