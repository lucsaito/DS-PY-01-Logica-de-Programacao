import random
import re


def imprime_mensagem_abertura():
    print("#################################")
    print("###Vamos Jogar? Jogo da Forca!###")
    print("#################################")
# Função para carregar as palavras do jogo
def carrega_palavra_secreta():
    tema_valido = False

    while(not tema_valido):

        tema = int(input("(1) BL (2) KDRAMA (3) CDRAMA (4) LAKORNS \nQual tema você quer? "))
        palavras = []

        if(tema == 1):

            with open("bl.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    palavras.append(linha)

            numero = random.randrange(0, len(palavras))
            palavra_secreta = palavras[numero].upper()
            tema_valido = True

        elif(tema == 2):

            with open("kdrama.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    palavras.append(linha)

            numero = random.randrange(0, len(palavras))
            palavra_secreta = palavras[numero].upper()
            tema_valido = True

        elif(tema == 3):

            with open("cdrama.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    palavras.append(linha)

            numero = random.randrange(0, len(palavras))
            palavra_secreta = palavras[numero].upper()
            tema_valido = True
        
        elif(tema == 4):

            with open("lakorns.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    palavras.append(linha)

            numero = random.randrange(0, len(palavras))
            palavra_secreta = palavras[numero].upper()
            tema_valido = True

        else:

            palavra_secreta = ("Opção Inválida!!! \nEscolha entre as opções disponíveis!")
            tema_valido = False
        
    return palavra_secreta

def iniciando_letras_certas(palavra):
    return ["_" if re.findall('[A-Z]', index) else '_' if re.findall ('[0-9]', index) else index for index in palavra]


def pedindo_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def marcando_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def mensagem_vencedor():
    print("Parabéns, você ganhou!")

def mensagem_perdedor(palavra_secreta):
    print("Você perdeu!")
    print(f'A palavra era {palavra_secreta}')

def desenhando_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_certas = iniciando_letras_certas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_certas)

    print(''.join(letras_certas))
    while (not acertou and not enforcou):

        chute = pedindo_chute()

        if (chute in palavra_secreta):
            marcando_chute_correto(chute, letras_certas, palavra_secreta)
            letras_faltando = str(letras_certas.count('_'))
            if (letras_faltando == "0"):
                print(f"PARABÉNS!! Você encontrou todas as letras formando a palavra '{palavra_secreta.upper()}'")
        else:
            erros += 1
            print(''.join(letras_certas))
            print(f'Ainda faltam acertar {letras_faltando} letras')
            print(f'Você ainda tem {7-erros} tentativas')
            desenhando_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_certas

        print(''.join(letras_certas))

    if (acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()
