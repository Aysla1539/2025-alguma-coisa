saldo = 0
extrato = []
def ver_saldo():

    global saldo
    print(f"\nSeu saldo atual é R${saldo}")

def depositar_valor():

    global saldo
    valor = float(input("\nInforme o valor a ser depositado: "))

    if valor <= 0:
        extrato.append(f"Depósito: Erro ao depositar R${valor}")
        print("Erro! Valor inválido.")

    else:
        saldo += valor
        extrato.append(f"Depósito: R${valor}")
        print(f"\nR${valor} depositado com sucesso!")
        print(f"Seu saldo atual é de R${saldo}")

def sacar_valor():

    global saldo
    valor = float(input("Informe o valor a ser sacado: "))
    
    if valor > saldo or valor <=0:
        extrato.append(f"Saque: Erro ao sacar R${valor}")
        print(f"Erro! Valor inválido. Você so tem R${saldo}")

    else:
        saldo -= valor
        extrato.append(f"Saque: R${valor}")
        print(f"R${valor} sacado com sucesso!")
        print(f"Seu saldo atual é de R${saldo}")

def ver_extrato():
    global saldo
    for movimentacao in extrato:
        print(movimentacao)
    print(f"Seu saldo e de R${saldo}")


def encerrar_conta():
    global saldo
    if saldo > 0:
        extrato.append(f"Saque: R${saldo}")
        saldo = 0 
    ver_saldo()
    print("Conta encerrada.")

def mostrar_menu():

    opcao = 0

    while(opcao != 5):

        print("\n1- Ver saldo\n2- Depositar valor\n3- Sacar valor\n4- Ver extrato\n5- Encerrar conta. ")
        opcao = int(input("\nEscolha a opção que deseja: "))

        if (opcao == 1):
            ver_saldo()
        elif (opcao == 2):
           depositar_valor()
        elif (opcao == 3):
            sacar_valor()
        elif(opcao == 4):
            ver_extrato()
        elif(opcao == 5):
            encerrar_conta()
        else:
            print("Opção inválida.")
print("--------Sistema de Gerenciamento Báncario--------")


mostrar_menu()
