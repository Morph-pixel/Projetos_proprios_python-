import random
opcoes = [
    'casa', 'cachorro', 'gato', 'computador', 'telefone',
    'janela', 'porta', 'mesa', 'cadeira', 'escola',
    'professor', 'aluno', 'livro', 'caderno', 'caneta',
    'bicicleta', 'carro', 'aviao', 'navio', 'estrada',
    'montanha', 'floresta', 'praia', 'deserto', 'rio',
    'oceano', 'planeta', 'estrela', 'galaxia', 'universo',
    'futebol', 'basquete', 'musica', 'filme', 'teatro',
    'comida', 'chocolate', 'sorvete', 'pizza', 'hamburguer',
    'banana', 'laranja', 'abacaxi', 'morango', 'melancia',
    'relogio', 'dinheiro', 'viagem', 'aventura', 'amizade',
    'computacao', 'programacao', 'algoritmo', 'variavel', 'funcao',
    'internet', 'teclado', 'monitor', 'codigo', 'software',
    'eletricidade', 'gravidade', 'temperatura', 'velocidade', 'labirinto',
    'biblioteca', 'restaurante', 'fotografia', 'instrumento', 'desenvolvimento',
    'paralelepipedo', 'otorrinolaringologista', 'inconstitucionalissimamente'
]
palavra = random.choice(opcoes) 
forca = palavra.replace('',' ').strip()
forca = forca.split(' ')
forca_visual = ['_' for caracter in forca] 
print(forca_visual) 
vida = 6
letra_usada = []
while True:
    letra = input('Qual letra ou a resposta?').strip().lower()
    if letra == '':
       print('Você não escreveu nada, tente novamente')
    elif letra == palavra:
       print(f'Parabéns, você acertou! A palavra era {palavra}')
       break 
    elif len(letra) > 2: 
           print('Não é essa palavra')
    elif len(letra) > 1: 
       print('Digite somente uma letra')
    elif letra in letra_usada:
       print('Essa letra já foi usada,tente outra')
    elif letra in palavra:
        letra_usada.append(letra)
        for lugar, caracter in enumerate(forca):
            if caracter == letra:
             forca_visual[lugar] = letra
        print(f'Acertou,{letra} está na palavra\n{forca_visual}\nLetras usadas:{letra_usada}')
        if '_' not in forca_visual:
            print(f'Parabéns, você acertou! A palavra era {palavra}')
            break
    else:
       letra_usada.append(letra)
       vida = vida - 1 
       print(f'Errou,{letra} não está na palavra. Você ainda tem {vida} vidas\n{forca_visual}\nLetras usadas{letra_usada}')
       if vida == 0: 
            print(f'Você morreu! a palavra era {palavra}')
            break     