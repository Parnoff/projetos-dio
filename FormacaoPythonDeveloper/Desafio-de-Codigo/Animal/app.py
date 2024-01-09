tipo_animal = {
    'vertebrado' : {
        'ave' : {
            'carnivoro' : {
              'aguia'    
            },
            'onivoro' : {
              'pomba'
            }
        },
        'mamifero' : {
            'onivoro' : {
              'homem' 
            }, 
            'herbivoro' : {
              'vaca'
            }
        }
    }, 
    'invertebrado': {
        'inseto' : {
          'hematofago' : {
            'pulga'      
          },
          'herbivoro' : {
            'lagarta'
          }
        },
        'anelideo' : {
          'hematofago' : {
            'sanguessuga'      
          },
          'onivoro' : {
            'minhoca'
          }            
        }        
    }
}

a = input()
b = input()
c = input()

resultado = str(next(iter(tipo_animal[a][b][c])))

print(resultado)






