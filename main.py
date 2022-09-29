from random import choice

vocabulario = ["canjica", "lagosta", "caju", "buchada", "fortaleza", "cachaça", "rapadura"]

palavra = choice(vocabulario)

print("\nJOGO DA FORCA\n")


chances = 5
alfabeto = ("abdcefghijklmnopqrstuvwxyzç")
tentativas = []

while chances !=0:
    print(f'Sua lista de tentativas é: {tentativas}')
    print("Chances restantes: ", chances)
    impressao =""

    #Bloco for para imprimir as listras e a letra
    for letra in palavra:
        if (letra in tentativas):
            impressao += letra
        else:
            impressao += " _"
    print(f'\n{impressao}')

    #Palpite da letra
    palpite = input(f"\nDigite seu palpite ou 'SAIR' para sair do programa!:  ").lower()

    #Condicionais de validação com a variável palpite recebida
    if palpite == "sair":
        break
    elif palpite not in alfabeto or palpite == '' or len(palpite) >1:
        print("Caractere digitado inválido, favor digitar uma letra do alfabeto!")
        continue
    elif palpite in tentativas:
        print(f"\nLetra já digitada!\n")
        continue
    else:
        tentativas.append(palpite)

    #Condicional para verificar se o palpite está na palavra selecionada
    if palpite in palavra:
        print(f"Palpite correto: {palpite}")
    else:
        print(f"Errou, o numero de tentativas irá diminuir!\n")
        chances-=1

    #Verificar a quantidade de chances
    if chances == 0 :
        print("Perdeu...\nFIM DO JOGO")
        print(f'Suas tentativas foram: {tentativas}')

    elif set(palavra).issubset(tentativas):
        print(f"\nParabéns, você acertou! A palavra correta é: {palavra.upper()}")
        break
