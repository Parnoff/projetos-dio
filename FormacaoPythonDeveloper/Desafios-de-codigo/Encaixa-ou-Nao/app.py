n = int(input())

while(n > 0):
  A, B = input().split()

  # Verifica se B é uma substring final de A
  if A.endswith(B):
    print("encaixa")
  else:
    print("nao encaixa")
        
  n -= 1

while(n > 0):
    entrada = input()

    valor_a, valor_b = entrada.split()

    if valor_b in valor_a:
        print('encaixa')
    else: 
        print('não encaixa') 
            
    n -= 1


'''
while(n > 0):

    valor_a = int(input("Valor de A? "))
    valor_b = int(input("Valor de B? "))

    if (valor_a <= 0 or valor_b <= 0) or ((len(str(valor_a)) > 1000 or len(str(valor_b)) > 1000)):
        print(f'Os valores de {valor_a} ou {valor_b} são <= 0 ou possuem mais de 1000 digitos!')
    else:
        str_valor_a = str(valor_a)
        str_valor_b = str(valor_b)

        if str_valor_b in str_valor_a:
            print('encaixa')
        else: 
            print('não encaixa') 

    n -= 1


while(n > 0):

    valor_a = int(input("Valor de A? "))
    valor_b = int(input("Valor de B? "))

    str_valor_a = str(valor_a)
    str_valor_b = str(valor_b)

    if str_valor_b in str_valor_a:
        print('encaixa')
    else: 
        print('não encaixa') 
            
    n -= 1
'''

