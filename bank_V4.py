from abc import ABC, abstractmethod
from datetime import datetime, date

class Transacao(ABC):
    @abstractmethod
    def saldo(self):
        pass

    @abstractmethod
    def deposito(self, valor):
        pass

    @abstractmethod
    def saque(self, valor):
        pass

class RealizarTransacao(Transacao):
    def __init__(self, conta):
        self._conta = conta

    def saldo(self):
        return self._conta.saldo()

    def deposito(self, valor):
        return self._conta.depositar(valor)

    def saque(self, valor):
        return self._conta.sacar(valor)

class Historico:
    def __init__(self):
        self._transacoes = {}

    def adicionar_transacao(self, transacao):
        dia = date.today()
        horario = datetime.now().time().strftime("%H:%M:%S")
        if dia not in self._transacoes:
            self._transacoes[dia] = {}
        self._transacoes[dia][horario] = transacao

    def mostrar(self):
        if self._transacoes:
            print("===== Extrato =====")
            for dia, transacoes in self._transacoes.items():
                print(f"Data: {dia}")
                for horario, transacao in transacoes.items():
                    print(f"  Hora: {horario} - {transacao}")
            print("===================")
        else:
            print("Nenhuma operação realizada")

class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    def saldo(self):
        return self._saldo

    def verificar_float(self, valor):
        """Converte a entrada em float, arredondando para 2 casas decimais."""
        try:
            return round(float(valor), 2)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            return None

    def depositar(self, valor):
        valor_deposito = self.verificar_float(valor)
        if valor_deposito is None or valor_deposito <= 0:
            print("Valor inválido. O valor deve ser positivo.")
            return False
        self._saldo += valor_deposito
        transacao = f"R$ + {valor_deposito:.2f}"
        self._historico.adicionar_transacao(transacao)
        print(f"Valor depositado: R$ + {valor_deposito:.2f}")
        return True

    def sacar(self, valor):
        valor_saque = self.verificar_float(valor)
        if valor_saque is None or valor_saque <= 0:
            print("Valor inválido. O valor deve ser positivo.")
            return False
        if valor_saque > 500:
            print("Limite máximo de saque é R$500.00")
            return False
        if valor_saque > self._saldo:
            print("Saldo insuficiente.")
            return False
        self._saldo -= valor_saque
        transacao = f"R$ - {valor_saque:.2f}"
        self._historico.adicionar_transacao(transacao)
        print(f"Valor sacado: R$ - {valor_saque:.2f}")
        return True

class Cliente:
    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        transacao._conta = conta

    def adicionar_conta(self, conta):
        self._contas.append(conta)

    def encontrar_conta(self, numero_conta):
        for conta in self._contas:
            if conta._numero == numero_conta:
                return conta
        return None

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

def gerar_numero_conta(clientes):
    """Gera um novo número de conta com base na quantidade de clientes existentes."""
    return f"0001{len(clientes) + 1:04d}"

clientes = []
cliente_logado = None
running = True

def mostrar_menu():
    if cliente_logado:
        menu = """Selecione uma função:
[D] Depósito
[S] Saque
[E] Extrato
[O] Sair da conta
[Q] Sair do sistema
"""
    else:
        menu = """Selecione uma função:
[L] Logar em uma conta
[C] Criar uma conta
[Q] Sair do sistema
"""
    return menu

while running:
    menu = mostrar_menu()
    escolha = input(menu).lower()
    
    if escolha == "c":
        cpf = input("Declare o CPF do titular da conta: ")
        if any(cliente._cpf == cpf for cliente in clientes):
            print("CPF já cadastrado.")
            criar_conta_com_usuario_existente = input("Gostaria de cadastrar outra conta? (Y/N): ")
            if criar_conta_com_usuario_existente.lower() == "y":
                nome = input("Declare o nome do titular da conta: ")
                data_nascimento = input("Declare a data de nascimento do titular da conta: ")
                endereco = input("Declare o endereço do titular da conta: ")
                novo_cliente = PessoaFisica(cpf, nome, data_nascimento, endereco, [])
                numero_conta = gerar_numero_conta(clientes)
                nova_conta = Conta(0.0, numero_conta, "Agência 0001", novo_cliente)
                novo_cliente.adicionar_conta(nova_conta)
                clientes.append(novo_cliente)
                print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
            else:
                entrar = input("Gostaria de entrar em sua conta? (Y/N): ")
                if entrar.lower() == "y":
                    numero_conta = input("Digite o número da conta: ")
                    cliente_logado = None
                    for cliente in clientes:
                        cliente_logado = cliente.encontrar_conta(numero_conta)
                        if cliente_logado:
                            print("Login realizado com sucesso!")
                            break
                    if not cliente_logado:
                        print("Falha ao logar. Por favor, verifique o número da conta e tente novamente.")
                else:
                    print("Retornando para o menu principal")
        else:
            nome = input("Declare o nome do titular da conta: ")
            data_nascimento = input("Declare a data de nascimento do titular da conta: ")
            endereco = input("Declare o endereço do titular da conta: ")
            novo_cliente = PessoaFisica(cpf, nome, data_nascimento, endereco, [])
            numero_conta = gerar_numero_conta(clientes)
            nova_conta = Conta(0.0, numero_conta, "Agência 0001", novo_cliente)
            novo_cliente.adicionar_conta(nova_conta)
            clientes.append(novo_cliente)
            print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

    elif escolha == "l":
        if cliente_logado:
            print("Você já está logado em uma conta.")
        else:
            cpf = input("Declare o CPF do titular da conta: ")
            cliente_logado = None
            for cliente in clientes:
                if cliente._cpf == cpf:
                    numero_conta = input("Digite o número da conta: ")
                    cliente_logado = cliente.encontrar_conta(numero_conta)
                    if cliente_logado:
                        print("Login realizado com sucesso!")
                        break
            if not cliente_logado:
                print("Falha ao logar. Por favor, verifique o CPF e o número da conta e tente novamente.")
        
    elif escolha == "d":
        if cliente_logado:
            valor_deposito = input("Digite o valor do depósito: R$ ")
            cliente_logado.depositar(valor_deposito)
        else:
            print("Nenhuma conta logada")
            
    elif escolha == "s":
        if cliente_logado:
            valor_saque = input("Digite o valor do saque: R$ ")
            cliente_logado.sacar(valor_saque)
        else:
            print("Nenhuma conta logada")
            
    elif escolha == "e":
        if cliente_logado:
            cliente_logado._historico.mostrar()
            print(f"Saldo: R${cliente_logado.saldo():.2f}")
        else:
            print("Nenhuma conta logada")
    
    elif escolha == "o":
        if cliente_logado:
            print(f"Você saiu da conta {cliente_logado._numero}.")
            cliente_logado = None
        else:
            print("Nenhuma conta logada para sair.")
    
    elif escolha == "q":
        print("Saindo do sistema...")
        running = False
