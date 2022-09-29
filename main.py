import random

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

            with open("lakorn.txt", "r", encoding="utf-8") as arquivo:
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
def inicializa_letras_acertadas(palavra):
    #alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    #for index in palavra:
        #if index == alfabeto:
    return ["_" for index in palavra]
        #else:
            #return [index for index in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Você perdeu!")
    print(f'A palavra era {palavra_secreta}')

def desenha_forca(erros):
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

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            letras_faltando = str(letras_acertadas.count('_'))
            if (letras_faltando == "0"):
                print(f"PARABÉNS!! Você encontrou todas as letras formando a palavra '{palavra_secreta.upper()}'")
        else:
            erros += 1
            print(letras_acertadas)
            print(f'Ainda faltam acertar {letras_faltando} letras')
            print(f'Você ainda tem {7-erros} tentativas')
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")

if(__name__ == '__main__'):
    jogar()
