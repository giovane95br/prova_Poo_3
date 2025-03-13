class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f'Valor de R${valor:,.2f} depositado com sucesso!'
        return "Valor inválido para depósito."

    def sacar(self, valor):
        if valor > self.__saldo:
            return "Saldo insuficiente!"
        elif valor > 0:
            self.__saldo -= valor
            return f'Saque de R${valor:,.2f} realizado com sucesso!'
        return "Valor inválido para saque."

    def get_dados(self, senha):
        if senha == 123:
            return f'Titular: {self.__titular} - Saldo: R${self.__saldo:,.2f} Disponível.'
        return "Senha incorreta!"

    def get_titular(self):
        return self.__titular


class DadosBancarios:
    def __init__(self):
        self.contas = {}

    def cadastrar_usuario(self):
        titular = input("Digite o nome do titular: ")
        saldo = float(input("Digite o saldo inicial: "))

        if titular in self.contas:
            print("Já existe uma conta com esse nome!")
        else:
            nova_conta = ContaBancaria(titular, saldo)
            self.contas[titular] = nova_conta
            print(f"Conta de {titular} cadastrada com sucesso!")

    def selecionar_conta(self, titular):
        return self.contas.get(titular, None)


# Menu interativo
dados = DadosBancarios()
conta_atual = None

while True:
    print("\n[1] Cadastrar Conta")
    print("[2] Selecionar Conta")
    print("[3] Depósito")
    print("[4] Saque")
    print("[5] Dados da Conta") #senha 123
    print("[6] Encerrar")

    opcao = int(input("O que gostaria de fazer? "))

    if opcao == 1:
        dados.cadastrar_usuario()

    elif opcao == 2:
        titular = input("Digite o nome do titular da conta: ")
        conta_atual = dados.selecionar_conta(titular)

        if conta_atual:
            print(f"Conta de {titular} selecionada!")
        else:
            print("Conta não encontrada.")

    elif opcao == 3:
        if conta_atual:
            valor = float(input("Digite o valor para depósito: "))
            print(conta_atual.depositar(valor))
        else:
            print("Selecione uma conta primeiro.")

    elif opcao == 4:
        if conta_atual:
            valor = float(input("Digite o valor para saque: "))
            print(conta_atual.sacar(valor))
        else:
            print("Selecione uma conta primeiro.")

    elif opcao == 5:
        if conta_atual:
            senha = int(input("Digite sua senha: "))
            print(conta_atual.get_dados(senha))
        else:
            print("Selecione uma conta primeiro.")

    elif opcao == 6:
        print("Encerrando...")
        break

    else:
        print("Opção inválida, tente novamente.")
