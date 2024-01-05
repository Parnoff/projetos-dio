menu = '''
      Bem vindo ao nosso sistema do Banco TopBank! 

      Em que podemos lhe ajudar hoje?

      Digite:
        [d] - Depósitos
        [s] - Saques
        [e] - Extratos
        [q] - Sair
        
=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
msg_retornar_menu = 'Retornando ao Menu principal'
msg_opcao_invalida = 'Opção inválida!'
movimentacaoes = {}

while True:

    opcao = input(menu)

    if opcao == 'd':
        
        while True:

            menu_deposito = 'Bem vindo a nossa seção de depósitos!\nEscolha uma opção:\n    [0] - Retornar ao menu principal\n    [1] - Realizar depósito em conta\n=> '
            opcao_deposito = int(input(menu_deposito))

            if opcao_deposito == 0:
                print(msg_retornar_menu)
                break
            elif opcao_deposito == 1:
                valor_deposito = 0
                valor_deposito = int(input('Digite o valor do depósito  R$: '))
                if valor_deposito > 0:
                    saldo += valor_deposito
                    print(f'Operação realizada com sucesso, foram depositados R$ {valor_deposito} em sua conta')
                    movimentacaoes[valor_deposito] = "Depósito"
                else:
                    print('O valor informado para o depósito é inválido! Por gentileza repita a operação...')
            else:
               print(msg_opcao_invalida) 

    elif opcao == 's':

        while True:

            menu_saque = 'Bem vindo a nossa seção de saques!\nEscolha uma opção:\n    [0] - Retornar ao menu principal\n    [1] - Realizar um saque\n=> '
            opcao_saque = int(input(menu_saque))

            if opcao_saque == 0:
                print(msg_retornar_menu)
                break
            elif opcao_saque == 1:
                valor_saque = 0
                valor_saque = int(input('Digite o valor do saque  R$: '))
                if valor_saque > 0 and valor_saque <= limite:
                    while True:
                        if numero_saques == LIMITE_SAQUES:
                            print(f'Seu limite de {LIMITE_SAQUES} saques diários foi excedido!\n')
                            break
                        else:
                            if valor_saque <= saldo:
                                saldo -= valor_saque
                                print(f'Operação realizada com sucesso, foram sacados R$ {valor_saque} da sua conta!\n')
                                movimentacaoes[valor_saque] = "Saque"
                                break
                            else:
                                print(f'Valor do Saque R$ {valor_saque}, saldo disponível R$ {saldo} a operação será cancelada!\n')
                                break
                    numero_saques += 1
                else:
                    print(f'O valor informado para o saque é inválido e/ou o Limite de Saque diário de R$ {limite} foi excedido!\n')
            else:
               print(msg_opcao_invalida) 

    elif opcao == 'e':
        while True:

            menu_extrato = 'Bem vindo a nossa seção de extratos!\nEscolha uma opção:\n    [0] - Retornar ao menu principal\n    [1] - Consultar o extrato da conta\n=> '
            opcao_extrato = int(input(menu_extrato))

            if opcao_extrato == 0:
                print(msg_retornar_menu)
                break
            elif opcao_extrato == 1:
                for valor, descricao in movimentacaoes.items():
                    if descricao == 'Saque':
                        print(f'{descricao} de - R$ {valor}')
                    else:
                        print(f'{descricao} de + R$ {valor}')
                        
                print(f'O saldo da sua conta é R$ {saldo}\n')
            else:
               print(msg_opcao_invalida) 

    elif opcao == 'q':
        break

    else:
        print(msg_opcao_invalida)
    







