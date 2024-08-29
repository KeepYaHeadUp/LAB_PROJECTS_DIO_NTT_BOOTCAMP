from datetime import datetime, date


data_atual = date.today()
tempo_atual = datetime.now().time()
clientes = []
running = True

menu = """Selecione uma função:
[L] Logar em uma conta
[C] Criar uma conta
[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair
"""

def criar_conta(cpf, clientes):
    nova_conta = {
        "numero da conta": str("0001" + str(len(clientes) + 1)),
        "nome": input("Declare o nome do titular da conta: "),
        "data de nascimento": input("Declare a data de nascimento do titular da conta: "),
        "cpf": cpf,
        "endereco": input("Declare o endereço do titular da conta: "),
        "historico": {},
        "saldo": 0.0
    }
    clientes.append(nova_conta)
    print("Conta criada com sucesso")
    return nova_conta

def logar(cpf, clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("Login efetuado com sucesso")
            return cliente
    print("Falha ao logar. Por favor, verifique o CPF e tente novamente.")
    return None

def inserir_data(transacao, cliente):
    dia = date.today()
    horario = datetime.now().time().strftime("%H:%M:%S")
    if dia not in cliente["historico"]:
        cliente["historico"][dia]= {}
    cliente["historico"][dia][horario] = transacao


def deposito(valor_deposito, login):
    if valor_deposito <= 0:
        print("Valor inválido.")
        return
    transacao = f"R$ + {valor_deposito:.2f}"
    inserir_data(transacao, login)
    login["saldo"] += float(valor_deposito)
    print(f"Valor depositado: R$ + {valor_deposito:.2f}")

def saque(valor_saque, cliente):
    if valor_saque > 500:
        print("Limite máximo de saque R$500.00")
        return
    if valor_saque > cliente["saldo"]:
        print("Saldo insuficiente")
        return
    
    transacao = f"R$ - {valor_saque:.2f}"
    inserir_data(transacao, cliente)
    cliente["saldo"] -= valor_saque
    print(f"Valor sacado: R$ - {valor_saque:.2f}")

def extrato(historico, saldo):
    if historico:
        print("=====Extrato=====")
        for dia, transacoes in historico.items():
            print(f"Data: {dia}")
            for horario, transacao in transacoes.items():
                print(f"  Hora: {horario} - {transacao}")
        print(f"Saldo R${saldo:.2f}")
        print("=================")
    else:
        print("Nenhuma operação realizada")


def verificar_float(valor):
    try:
        return round(float(valor), 2)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return None

cliente_logado = None

while running:
    escolha = input(menu).lower()
    if escolha == "c":
        cpf = input("Declare o cpf do titular da conta: ")
        if any(cliente['cpf'] == cpf for cliente in clientes):
            print("CPF já cadastrado.")
            criar_conta_com_usuario_existente = input(
                "Gostaria de cadastrar outra conta? Y/N")
            if criar_conta_com_usuario_existente.lower() == "y":
                cliente_logado = criar_conta(cpf, clientes)
            else:
                entrar = input("Gostaria de entrar em sua conta? Y/N")
                if entrar.lower() == "y":
                    cliente_logado = logar(cpf, clientes)
                    print("Login realizado com sucesso!")
                else:
                    print("Retornando para o menu principal")
        else:
            cliente_logado = criar_conta(cpf, clientes)

    elif escolha == "l":
        cpf = input("Declare o cpf do titular da conta: ")
        cliente_logado = logar(cpf, clientes)
        
    elif escolha == "d":
        if cliente_logado:
            var_deposito = verificar_float(
                input("Digite o valor do depósito: R$"))
            if var_deposito is not None:
                deposito(valor_deposito=var_deposito,
                         login=cliente_logado)  #keyword argument
        else:
            print("Nenhuma conta logada")
    elif escolha == "s":
        if cliente_logado:
            valor_saque = verificar_float(input("Digite o valor do saque: R$"))
            if valor_saque is not None:
                saque(valor_saque, cliente_logado)  #positional arugment
        else:
            print("Nenhuma conta logada")
    elif escolha == "e":
        if cliente_logado:
            extrato(historico=cliente_logado["historico"],
                    saldo=cliente_logado["saldo"])
        else:
            print("Nenhuma conta logada")
    elif escolha == "q":
        print("Saindo...")
        running = False
