# sistema_bancario.py

from conta import Conta
from operacoes import realizar_deposito, realizar_saque, exibir_extrato

def menu():
    print("\n===== Bem-vindo ao Banco Python =====")
    print("1. Criar Conta")
    print("2. Depósito")
    print("3. Saque")
    print("4. Extrato")
    print("5. Sair")

def main():
    contas = {}

    while True:
        menu()
        opcao = input("\nDigite a opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do titular: ")
            cpf = input("Digite o CPF do titular: ")
            senha = input("Digite a senha da conta: ")
            conta = Conta(nome, cpf, senha)
            contas[conta.numero] = conta
            print(f"\nConta criada com sucesso! Número da conta: {conta.numero}")

        elif opcao == "2":
            realizar_deposito(contas)

        elif opcao == "3":
            realizar_saque(contas)

        elif opcao == "4":
            exibir_extrato(contas)

        elif opcao == "5":
            print("Obrigado por utilizar o Banco Python!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()