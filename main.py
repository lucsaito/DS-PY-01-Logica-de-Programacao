from random import choice

vocabulario = ['arvore', 'banana', 'gato', 'churrasqueira']

palavra = choice(vocabulario)

print("DESAFIO MODULO 1 HANGMAN (Jogo da Forca)\n")
print("JOGO DA FORCA. Boa sorte!\n")

chances = 3
alfabeto = list("abdcefghijklmnopqrstuvwxyz")
tentativas = []

while True:
  print(tentativas)
  print("Chances: ",chances)

  for letra in palavra:
    if letra in tentativas:
      print(letra, end = ' ')
    else:
      print('_', end= ' ')

  palpite = input("\nDigite uma letra ").lower()
  if palpite not in alfabeto or palpite == '':
    print("Digite um caractere válido")
    continue	
  elif palpite in tentativas:
    print("ih rapaz, tu já escreveu essa letra. Tenta outra!")
    continue
  tentativas.append(palpite)
  if palpite in palavra:
    print("Boa!")
  else:
    print("Rapazzz!")
    chances-=1
  if chances == 0:
    print("Suas tentativas acabaram :(")
    break
  elif set(palavra).issubset(set(tentativas)):
    palavra = palavra.upper()
    print(palavra)
    print("Parabéns! Você descobriu a palavra.")
    break
