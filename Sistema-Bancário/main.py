# Depósito, saque e extrato
# Depósito = valor a ser acrescentado guardando em uma variável
# Saque Valor a ser debitado
# Extrato = resultado das operações
# Operação de depósito:
    # O sistema deve permitir realizar 3 saques diários com limite máximo de 500 Reais por saque
    # Caso não tenha saldo em conta, o sistema deve exibir uma mensagem

saldo = 0
vezes = 3
limite = 500
senha = int(input("Insira sua senha: "))

if senha == 12345678:
    print("=========== Bem-vindo! ===========")
    print("\n")
    
    while True:
        print("O que você quer fazer hoje?\n")
        print("Digite:\n[1] - Saque\n[2] - Depósito\n[3] - Extrato\n")
        
        ope = input("")

        if ope == "1":
            if vezes == 0:
                print("Apenas 3 saques por dia!\n")
            else:
                saque = int(input("Valor a ser sacado: "))
                print("\n")
                if saque > saldo:
                    print("Saldo insuficiente!\n")
                elif saque > limite:
                    print(f"Limite de saque diário excedido (limite: R$ {limite})!\n")
                else:
                    saldo -= saque
                    vezes -= 1
                    print(f"Saque de R$ {saque:.2f} realizado com sucesso!\n")

        elif ope == "2":
            depo = float(input("Insira o valor do depósito (apenas números positivos): "))
            if depo <= 0:
                print("Valor de depósito inválido! Insira apenas valores positivos.\n")
            else:
                saldo += depo
                print(f"Depósito de R$ {depo:.2f} realizado com sucesso!\n")

        elif ope == "3":
            print(f"Seu saldo é de R$ {saldo:.2f}\n")

        else:
            print("Opção inválida!\n")

else:
    print("Senha Incorreta")

            


    
    
   


