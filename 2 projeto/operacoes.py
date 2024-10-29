# operacoes.py

def realizar_deposito(contas, numero_conta, valor):
    conta = contas.get(numero_conta)
    if conta:
        conta.saldo += valor
        conta.extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def realizar_saque(contas, numero_conta, valor):
    conta = contas.get(numero_conta)
    if conta:
        if conta.saldo >= valor:
            conta.saldo -= valor
            conta.extrato.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")

def exibir_extrato(contas, numero_conta):
    conta = contas.get(numero_conta)
    if conta:
        print("\n===== Extrato Bancário =====")
        print(f"Titular: {conta.titular}")
        print(f"CPF: {conta.cpf}")
        print(f"Número da conta: {conta.numero}")
        print(f"Saldo: R$ {conta.saldo:.2f}")
        print("\nHistórico de operações:")
        if conta.extrato:
            for operacao in conta.extrato:
                print(operacao)
        else:
            print("Nenhuma operação realizada.")
    else:
        print("Conta não encontrada.")