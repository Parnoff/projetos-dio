
def sacar():
    print('Function de sacar')

def depositar():
    print('Function de depositar')

def extrato():
    print('Function do extrato')

def cadastrar_user():
    print('Function do cadastro user')

def cadastrar_acc_bancaria():
    print('Function do cadastro de conta bancária')

def menu():
    return 'Function de acesso ao menu'

dados_contas = {
    '0001' : {
        '99999-9' : {
            '000.000.000-00'    
        }
    },
    '0002' : {
        '00001-5' : {
            '000.000.000-01'
        },
        '00002-5' : {
            '000.000.000-02'
        },
        '00003-5' : {
            '000.000.000-03'
        }
    }  
}

def login(agencia, conta):
    if agencia in dados_contas:
        if conta in dados_contas[agencia]:
            return menu()
        else:
            print('Conta inexistente.') 
    else:
        print('Agência inexistente.')  


#print(login('000.000.000-00','0001','99999-9'))

#print(dados_contas)

print(login('0002','00002-5'))
        
#print(dados_contas['0003'])


