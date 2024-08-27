from datetime import datetime, date, time

# Variáveis iniciais
data_atual = date.today()
tempo_atual = datetime.now().time()

running = True
historico = {}
saldo = 0.0


menu = """Selecione a função:
[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair
"""

def inserir_data(transacao):
    dia = date.today()
    horario = datetime.now().time().strftime("%H:%M:%S")
    if dia not in historico:
        historico[dia] = {}  
    contagem_dic = len(historico[dia])
    if contagem_dic >= 10:
        print("Limite de transações diárias atingido.")  
        return False
    historico[dia][horario] = transacao



def deposito(valor_deposito, inserir_data):
    global saldo
    if valor_deposito <= 0:
        print("Valor inválido.")
        return
    transacao = f"R$ + {valor_deposito:.2f}"
    if inserir_data(transacao) == False:
        return
    saldo += valor_deposito
    print(f"Valor depositado: R$ + {valor_deposito:.2f}")
    return
def saque(valor_saque, inserir_data):
    global saldo
    if valor_saque > 500:
        print("Limite máximo de saque R$500.00")
        return
    elif valor_saque > saldo:
        print("Saldo insuficiente")
        return
    else:
        transacao = f"R$ - {valor_saque:.2f}"
        if inserir_data(transacao) == False:
            return        
        saldo -= valor_saque
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

while running: 
    escolha = input(menu).lower()
    if escolha == "d":
        valor_deposito = verificar_float(input("Digite o valor do depósito: "))
        if valor_deposito is not None:
            deposito(valor_deposito, inserir_data)
    elif escolha == "s":
        valor_saque = verificar_float(input("Digite o valor do saque: "))
        if valor_saque is not None:
            saque(valor_saque, inserir_data)

    elif escolha == "e":
        extrato(historico, saldo)

    elif escolha == "q":
        print("Saindo...")
        running = False
