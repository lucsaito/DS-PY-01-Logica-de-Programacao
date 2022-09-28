import random
palavras = ['UVA', 'BANANA', 'CACAU', 'MANGA', 'LARANJA', 'GOIABA', 'PITAYA', 'ABACAXI', 'KIWI', 'ABACATE', 'CEREJA']
palavra = random.choice(palavras)

tentativas = []
contador = 0
resultado = True

while(contador < 5):
  palpite = input(f"Digite uma letra ou 0 para encerrar os palpites. Você tem {5 - contador} tentativas: ").upper()
  if palpite == '0':
    break
  else:
    tentativas.append(palpite)
    impressao = ""
    for l in palavra:
      if(l in tentativas):
        impressao += l
      else:
        impressao += "_"
    print(impressao)
    contador += 1

if (impressao == palavra):
  resultado = True
elif (impressao != palavra):
  resultado = False

if (resultado == True):
  print('Parabéns, você acertou! A palavra é ' + impressao)
elif (resultado == False):
  print('Que pena! Você perdeu!')
else:
  pass
