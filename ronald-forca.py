import random
#gerar números aleatórios

palavras = ['abacate','chocolate','paralelepipedo','goiaba']
letrasErradas = ''
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def aula():
    while True:
        x = input('insira algo: ')
        palavras.append(x)
        if x == '':
            break
        
def principal():
#definir funções
    """
    Função Princial do programa
    """
    print('F O R C A')
    aula()
    #imprimir textos na tela

    palavraSecreta = sortearPalavra()
    palpite = ''
    desenhaJogo(palavraSecreta,palpite)

    while True:
        #enquanto for verdadeiro
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
        #se
            print('Voce Perdeu!!!')
            break
            #parar
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo():
    global FORCAIMG
    #aquela que não foi definida
    if len(letrasErradas) == len(FORCAIMG):
       #mede um número de elementos de uma lista ou string
        return True
        #retornar para True
    else:
    #senão
        return False
        #retornar para False
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    #aquela que não foi definida
    ganhou = True #verdadeiro
    for letra in palavraSecreta:
    #para     #em    
        if letra not in letrasCertas:
                #não estiver em
            ganhou = False
                    #falso
    return ganhou
    #retornar para
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
              #pedir uma informação ao usuário
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas:
    #junção de else com if      #ou
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z":
    #contrário de elif
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
        #para a variável no alcance
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

    
principal()

