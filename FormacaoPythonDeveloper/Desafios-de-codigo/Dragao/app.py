''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
C = int(input("Quantidade de testes? ")) 
for i in range (C): 
    N = int(input("Qual o poder de luta? ")) 
    if N < 8001:
        print("Inseto!")
    else:
        print("Maior que 8000!")