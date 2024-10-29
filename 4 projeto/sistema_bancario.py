from cliente import Cliente
from conta import Conta

def menu():
    print("\n===== Bem-vindo ao Banco Python =====")
    print("1. Criar Cliente")
    print("2. Criar Conta")
    print("3. Depósito")
    print("4. Saque")
    print("5. Extrato")
    print("6. Sair")

def main():
    clientes = []
    
    while True:
        menu()
        opcao = input("\nDigite a opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            cliente = Cliente(nome, cpf)
            clientes.append(cliente)
            print(f"\nCliente {nome} criado com sucesso!")
        
        elif opcao == "2":
            cpf_cliente = input("Digite o CPF do cliente: ")
            cliente_encontrado = None
            for cliente in clientes:
                if cliente.cpf == cpf_cliente:
                    cliente_encontrado = cliente
                    break
            
            if cliente_encontrado:
                conta = Conta()
                cliente_encontrado.criar_conta(conta)
                print(f"Conta criada com sucesso! Número da conta: {conta.numero}")
            else:
                print("Cliente não encontrado.")

        elif opcao == "3":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do depósito: "))
            
            for cliente in clientes:
                for conta in cliente.contas:
                    if conta.numero == numero_conta:
                        conta.depositar(valor)
                        break
                else:
                    continue
                break
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            numero_conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do saque: "))

            for cliente in clientes:
                for conta in cliente.contas:
                    if conta.numero == numero_conta:
                        conta.sacar(valor)
                        break
                else:
                    continue
                break
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            numero_conta = int(input("Digite o número da conta: "))

            for cliente in clientes:
                for conta in cliente.contas:
                    if conta.numero == numero_conta:
                        conta.exibir_extrato()
                        break
                else:
                    continue
                break
            else:
                print("Conta não encontrada.")

        elif opcao == "6":
            print("Obrigado por utilizar o Banco Python!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()