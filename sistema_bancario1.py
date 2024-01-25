## Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

## Desafio 

# Fomos contratados por um grande banco para desenvolver o
# seu novo sistema. Esse banco deseja modernizar suas
# operações e para isso escolheu a linguagem Python. Para a
# primeira versão do sistema devemos implementar apenas 3
# operações: depósito, saque e extrato.

menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
valor_deposito = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
         valor_deposito = int(input("Valor a ser depositado? "))
         if valor_deposito >= 1:
            print("Deposito realizado!")
            saldo += valor_deposito
            print(f"Seu saldo é R${saldo}")
         elif valor_deposito <= 0:
            print("Valor incorreto!")
            
    elif opcao == "s":
        numero_saques += 1
        if numero_saques < LIMITE_SAQUES:
            saque = int(input(f"Qual valor deseja sacar do seu saldo R${saldo}? "))
            if saque <= 500:
                print(f"Saque realizado no valor R${saque}")
                saldo -= saque
            elif saque > 500:
                print("Valor do saque excedeu o limite de saque!")

        elif numero_saques > LIMITE_SAQUES:
            print("Você excedeu o limite de saque diário. Tente novamente mais tarde!")
           
    
    elif opcao == "e":
        print(f"Seu extrato é R${saldo}")

    elif opcao == "q":
        print("Saindo")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")