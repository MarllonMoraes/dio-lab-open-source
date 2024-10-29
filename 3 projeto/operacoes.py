# operacoes.py

def realizar_deposito(contas):
    numero_conta = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor do depósito: "))
    
    if numero_conta in contas:
        contas[numero_conta].depositar(valor)
    else:
        print("Conta não encontrada.")

def realizar_saque(contas):
    numero_conta = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor do saque: "))

    if numero_conta in contas:
        contas[numero_conta].sacar(valor)
    else:
        print("Conta não encontrada.")

def exibir_extrato(contas):
    numero_conta = int(input("Digite o número da conta: "))

    if numero_conta in contas:
        contas[numero_conta].exibir_extrato()
    else:
        print("Conta não encontrada.")