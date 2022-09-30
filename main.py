import random
# Declare suas funções abaixo


if __name__ == "__main__":
    # Adicione seu código abaixo e declare suas funções a serem usadas acima

# 1 passo: Estabelecer um número X de tantativas para o usuário tentar advinhar 
tentativas = 0
tentativas_max = 3

# 2 passo: Escolher uma palavra aleatória de uma lista por uma bilioteca "random"

import random

lista_de_palavras = ['arvore', 'banana', 'cachorro', 'laranja']
palavra_sorteada = random.choice(lista_de_palavras) #retorna um elemento da sequência sorteada
tamanho_palavra = len(palavra_sorteada) # saber quantas letras a palavra tem
print(f'{palavra_sorteada}\n')

    
# 3 passo: Mensagem de abertura 

print(f"Bem vindo ao jogo da forca! \n" 
      f"Você terá {tentativas_max} tentativas para chutar uma letra e advinhar qual é palavra escolhida aleatoriamente.\n" 
      f"Vamos começar!\n"
      f" \n"
      f"A palavra escolhida tem {tamanho_palavra} letras. \n")


# 4 passo: Os testes 

letras_acertadas = ["_" for letra in palavra_sorteada] # Cria uma lista em que para cada letra da palavra sorteada coloca um tracinha
letras_faltando = len(letras_acertadas) # para saber quantas palavras estão faltando

while (tentativas < tentativas_max):
    palpite = input('Digite uma letra: \n').lower()
         
    if (palpite in palavra_sorteada):
        index = 0
        for letra in palavra_sorteada:
            if (palpite == letra):
                letras_acertadas[index] = letra
            index += 1
        letras_faltando = str(letras_acertadas.count('_'))
        print(letras_acertadas)
        
        if (letras_faltando == "0"):
            print(f'Parabéns! Você encontrou todas as letras que formam a palavra "{palavra_sorteada.capitalize()}!"')
            break
       
        print(f'Ainda faltam acertar {letras_faltando} letras.')
            
    elif (palpite not in palavra_sorteada):
        tentativas += 1
        if (tentativas_max > tentativas):
            print(letras_acertadas)
            print(f'Ainda faltam acertar {letras_faltando} letras. \n'
                  f'Você ainda tem {tentativas_max-tentativas} tentativas. \n')
        
        elif (tentativas_max == tentativas):
            print(letras_acertadas)
            print(f'Faltou acertar {letras_faltando} letras, mas as tentativas acabaram e você perdeu!')
    else:
        pass

    
    print("Código a ser executado!")
