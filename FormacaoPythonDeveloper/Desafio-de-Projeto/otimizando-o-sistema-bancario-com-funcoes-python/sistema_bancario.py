import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor):
    saldo += valor
    return saldo

def sacar(saldo,valor):
    saldo -= valor
    return saldo   

def validar_valor():
    print("O valor digitado é menor ou igual a 0 (Zero)!")
        

def main():

    saldo = 0
    movimentacoes = {}

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo = depositar(saldo,valor)
                movimentacoes[valor] = "Depósito"
                print("Depósito de R$ ",valor," realizado com sucesso!")
            else:
                validar_valor()
        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            if valor > 0:
                if saldo - valor >= 0:
                    saldo -= sacar(saldo,valor)
                    movimentacoes[valor] = "Saque"
                    print("Saque de R$ ",valor," realizado com sucesso!") 
                else:
                    print("Seu saldo é insuficiente!")      
            else:
                validar_valor()   
        elif opcao == 'e':
            for valor, descricao in movimentacoes.items():
                if descricao == 'Saque':
                    print(f'{descricao} de - R$ {valor}')
                else:
                    print(f'{descricao} de + R$ {valor}')     
            print(f'O saldo da sua conta é R$ {saldo}\n')                      
        else:
            break

main()