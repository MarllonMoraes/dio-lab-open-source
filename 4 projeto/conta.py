class Conta:
    proximo_numero = 1

    def __init__(self):
        self.numero = Conta.proximo_numero
        Conta.proximo_numero += 1
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso!")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            print("Valor inválido para saque.")

    def exibir_extrato(self):
        print("\n===== Extrato Bancário =====")
        print(f"Número da conta: {self.numero}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("\nHistórico de operações:")
        if self.extrato:
            for operacao in self.extrato:
                print(operacao)
        else:
            print("Nenhuma operação realizada.")