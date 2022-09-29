# Joguinho da Forca - Hangman
# Natacha Stephany - Turma 894

import random

def mensagem_abertura(): # bem fofa
    print("\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F \
\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F")
    print("Joguinho da Forca. Está preparado?!")
    print("\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F \
\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F\u2764\uFE0F")

def bonequinhos_forca(chances):
    print("  _______     ")
    print(" |/      |    ")

    if(chances == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(chances == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(chances == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(chances == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(chances == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(chances == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (chances == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
  

palavras = ['estetoscopio', 'otorrinolaringologista', 'corinthians', 'hexacampeão' , 'natacha']
secreto = random.choice(palavras)
digitadas = []
chances = 7

mensagem_abertura()

while True:
    if chances <=0:
        print('Já era, você perdeu!!')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Te orienta! Digite apenas uma letra!')
        continue

    digitadas.append(letra) #acrescenta na lista
    if letra in secreto:
        print('A letra "{}" está dentro da palavra secreta!' .format(letra))
    else:
        print('A letra "{}" não existe na palavra secreta' .format(letra))
        digitadas.pop() #elimina a última na lista

    secreto_temporario = ''
    for letra_secreta in secreto: # Para letra secreta estiver em secreto
        if letra_secreta in digitadas: # se a letra está em digitadas
            secreto_temporario += letra_secreta # secreto temporario será a letra secreta que está conectada no secreto e digitadas
        else:
            secreto_temporario += '*' # Coloque * se estiver incorreta

    if secreto_temporario == secreto:
        print('Você é top! A palavra é "{}", parabéns pelo acerto!' .format(secreto_temporario))
        break
    else:
       print('Sua palavra está assim: {}' .format(secreto_temporario))
    
    if letra not in secreto:
      chances -= 1
      print('Você ainda tem {} chances.' .format(chances))
      bonequinhos_forca(chances)
