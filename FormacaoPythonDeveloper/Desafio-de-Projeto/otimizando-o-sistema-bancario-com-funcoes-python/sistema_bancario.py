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
clientes = []  # Lista vazia para armazenar informações dos clientes
def cadastrar_cliente(nome,data_nascimento,cpf,endereco):
    # Cria um dicionário com as informações do cliente
    cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }

    # Adiciona o dicionário à lista de clientes
    clientes.append(cliente)

def listar_clientes():
    # Imprime as informações dos clientes
    print("\nInformações dos clientes:")
    for cliente in clientes:
        print(f"\nNome: {cliente['nome']}")
        print(f"Data de Nascimento: {cliente['data_nascimento']}")
        print(f"CPF: {cliente['cpf']}")
        print(f"Endereço: {cliente['endereco']}")   

def cpf_existe(cpf):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print(f'CPF {cpf} já cadastrado!')
            return True
        else:
            return False
        
contas = []  # Lista vazia para armazenar informações das contas bancárias       
def cadastrar_conta(cpf):
    
    # Número da Agência está fixo
    AGENCIA = '0001'
    
    # Verifica se a lista está vazia
    if not contas:
        # Número das contas inicia em 1
        numero = 1
    else:
       numero = max(conta['numero'] for conta in contas) + 1

    # Cria um dicionário com as informações da conta
    conta = {
        'agencia': AGENCIA,
        'numero': numero,
        'cpf': cpf
    }

    # Adiciona o dicionário à lista de clientes
    contas.append(conta)

def listar_contas():
    print("\nInformações dos contas:")
    for conta in contas:
        print(f"\nAgência: {conta['agencia']}")
        print(f"Número: {conta['numero']}")
        print(f"CPF: {conta['cpf']}")

def main():

    saldo = 0
    movimentacoes = {}
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    msg = "O valor digitado é menor ou igual a 0 (Zero)!"

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo = depositar(saldo,valor)
                movimentacoes[valor] = "Depósito"
                print("Depósito de R$ ",valor," realizado com sucesso!")
            else:
                print(msg)
        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            if valor > 0:
                if (saldo - valor >= 0) and (numero_saques < LIMITE_SAQUES) and (valor <= limite):
                    saldo = sacar(saldo,valor)
                    numero_saques += 1
                    movimentacoes[valor] = "Saque"
                    print("Saque de R$ ",valor," realizado com sucesso!") 
                else:
                    print(f"""\n
                          ===========Atenção===========
                          Seu saldo é insuficiente! OU
                          Limite de Saques {LIMITE_SAQUES} diários foi atingido! OU
                          Valor R$ {limite} Limite de Saque foi atingido!
                          """)
            else:
                print(msg)   
        elif opcao == 'e':
            for valor, descricao in movimentacoes.items():
                if descricao == 'Saque':
                    print(f'{descricao} de - R$ {valor}')
                else:
                    print(f'{descricao} de + R$ {valor}')     
            print(f'O saldo da sua conta é R$ {saldo}\n')    
        elif opcao == 'nc':
            cpf = '101.471.869-43'
            cadastrar_conta(cpf)     
            listar_contas()  
        elif opcao == 'lc':
            print("Listando contas cadastradas!")       
        elif opcao == 'nu':
            nome = input("Digite o nome do cliente: ")
            data_nascimento = input("Digite a data de nascimento do cliente (formato: DD/MM/AAAA): ")
            cpf = input("Digite o CPF do cliente: ")
            if cpf_existe(cpf):
                continue
            else:
                endereco = input("Digite o endereço do cliente: ")
                cadastrar_cliente(nome,data_nascimento,cpf,endereco)
                listar_clientes()
        elif opcao == 'q':
            print("Até logo!") 
            break   
        else:
            print("Opção inválida")
            break

main()