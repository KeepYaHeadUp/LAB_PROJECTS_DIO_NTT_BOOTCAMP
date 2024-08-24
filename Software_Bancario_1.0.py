

#forma de exibiçao R$ xxx.xx
running = True
historico = ["Extrato"]
saldo = float()
LIMITE_DE_SAQUES_DIARIOS = 3
numero_de_saques = 0
saque_maximo = 500

menu = """Selecione a função:
[D] Deposito
[S] Saque
[E] Extrato
[Q] Sair
"""

def limite(numero_de_saques, limite = LIMITE_DE_SAQUES_DIARIOS):
  return numero_de_saques >= limite

def deposito(valor_deposito, extrato):
  global saldo
  if valor_deposito <= 0:
    print("Valor inválido.0")
    return
  print(f"Deposito realizado com sucesso. Saldo atual de R${saldo.2f}")
  saldo += float(valor_deposito)
  extrato.append(f"+ R${valor_deposito}")
  return

def saque(valor_saque, extrato):
  global numero_de_saques
  if limite(numero_de_saques):
    print("Limite de saques diários atingido")
    return
  else: 
    global saldo
    if valor_saque > 500:
        print("limite máximo de saque R$500.00")
        return
    elif valor_saque > saldo:
      print("Saldo insuficiente")
      return
  
    else:
        saldo -= valor_saque
        extrato.append(f"- R${valor_saque}")
        numero_de_saques += 1
        return
def extrato(historico, saldo): 
  #Exibir lista de todos depositos e saques realizados na conta, e no fim o saldo
  for i in historico:
    print(i)
  print(f"Saldo R${saldo.2f}")

def sair():
  print("Saindo...")
  global running
  running = False
while running: 
  escolha = input(menu).lower()
  if escolha == "d":
    var_deposito = round(float(input("Digite o valor do deposito: ")), 2)
    deposito(valor_deposito = var_deposito, extrato =  historico)

  elif escolha == "s":
    var_saque = round(float(input("Digite o valor do saque: ")), 2)
    saque(valor_saque = var_saque, extrato = historico)

  elif escolha == "e":
    extrato(historico, saldo)


  elif escolha == "q":
    sair()