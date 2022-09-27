import random

def letra_certa(letra: str) -> list:  
  for elemento in palavra_escolhida:
    if letra_do_usuario == elemento:
      lista_letras_corretas.append(letra)
  return lista_letras_corretas

def letra_errada(letra: str) -> list:
  if letra not in palavra_escolhida:
    lista_letras_erradas.append(letra)
  return lista_letras_erradas

def checar_letra(letra: str) -> bool:

  for i in lista_letras_corretas:
    if letra == i:
      print('Você já escolheu essa letra antes.\n')
      return True

  for i in lista_letras_erradas:
    if letra == i:
      print('Você já escolheu essa letra antes.\n')
      return True

  return False

def representacao_grafica () -> str:
  lista_representacao = []

  for elemento in palavra_escolhida:
    lista_representacao.append(elemento)
  
  for index, elemento in enumerate(lista_representacao):
    if elemento in lista_letras_corretas:
      lista_representacao[index] = elemento
    else:
      lista_representacao[index] = '_'
  
  representacao = ''.join(lista_representacao)
  print(f'''
  ---> Seu resultado até agora: {representacao}
  ''')
  return representacao

def checagem_acerto(representacao: str) -> bool:
  if representacao == palavra_escolhida:
    print(f'\nParabéns {nome_do_usuario}, você acertou a palavra {palavra_escolhida}!!!')
    return True
  else:
    return False


nomes_de_animais = ['GIRAFA', 'OVELHA', 'PINGUIM', 'POLVO', 'GALO', 'LEBRE', 'MINHOCA']
nomes_de_comida = ['AMENDOIM', 'QUEIJO', 'BROCOLIS', 'MELANCIA', 'CENOURA', 'BANANA', 'REPOLHO']
nomes_de_profissoes = ['PADEIRO', 'ATOR', 'PROFESSOR', 'AGRICULTOR', 'MOTORISTA', 'JORNALISTA', 'ADVOGADO']
categorias = ['Nomes de animais', 'Nomes de comida', 'Nomes de profissões']
categoria_escolhida = random.choice(categorias)

if categoria_escolhida == 'Nomes de animais':
  palavra_escolhida = random.choice(nomes_de_animais)
elif categoria_escolhida == 'Nomes de comida':
  palavra_escolhida = random.choice(nomes_de_comida)
else:
  palavra_escolhida = random.choice(nomes_de_profissoes)

quantidade_de_tentativas_erradas = 6
lista_letras_corretas = []
lista_letras_erradas = []


nome_do_usuario = input('''JOGO DA FORCA
Qual o nome do Jogador?
''')

print(f'''
Olá {nome_do_usuario}! Sua palavra tem {len(palavra_escolhida)} letras.
Sua dica é: {categoria_escolhida}.
Boa sorte!
''')

while quantidade_de_tentativas_erradas > 0:
  letra_do_usuario = input('Digite uma letra:\n').upper()

  while letra_do_usuario.isdigit():
    print(f'\n{nome_do_usuario}, você colocou um número. Tente novamente.\n')
    letra_do_usuario = input('Digite uma letra:\n').upper()    

  while checar_letra(letra_do_usuario):
    letra_do_usuario = input('Digite uma letra:\n').upper()

  if letra_do_usuario in palavra_escolhida:
     letra_certa(letra_do_usuario)
     grafico = representacao_grafica()
     if checagem_acerto(grafico):
       break
  else:
    letra_errada(letra_do_usuario)
    quantidade_de_tentativas_erradas -= 1
    if quantidade_de_tentativas_erradas == 0:
      print(f'''
      Que pena {nome_do_usuario}, você esgotou suas chances.
      A palavra era {palavra_escolhida}
      Você errou as letras {lista_letras_erradas}
      ''')
    else:
      print((f'''
      Você errou.
      Tente novamente, você ainda tem {quantidade_de_tentativas_erradas} chances
      Você já tentou as seguintes letras erradas: {lista_letras_erradas}
      '''))
      representacao_grafica()
