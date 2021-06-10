from cores import * 
import pygame
import random
# esse arquivo biblioteca já existia antes com o nome "peças", mas por dificuldades com a integração do código tudo foi juntado
# em um mesmo arquivo. com a finalização do projeto, dividimos novamente as classes e funções em outras bibliotecas para organização do 
# código. essa é a nova biblioteca, no arquivo chamado peças, que possui a classe Peca onde as peças são criadas, mas não geradas ainda.
# lista de cores para que as peças sejam de cores aleatórias. o comando random escolhe uma cor da lista e pinta o formato da peça com ela
cores = [
    CORES['preto'], # por algum motivo peças geradas com a primeira cor da lista desaparecem ao colidir com o tabuleiro *1
    CORES['azul'],
    CORES['verde'],
    CORES['verdao'],
    CORES['rosinha'],
    CORES['roxo'],
    CORES['laranja']

]
# essas cores são os valores do dicionário 'CORES' da biblioteca 'cores' criada para o projeto. 

class Peca:
    # nessa classe as peças do jogo são definidas com valores de posição estilo matriz. 
    # cada lista tem a lista principal com a posição padrão da peça seguido pelas variações de posição desse mesmo formato
    # types define os tipos de peça. cada lista de peça recebe uma lista de coordenadas principais ([1]) e, se a peça pode ser
    # rotacionada, as diferentes posições da peça, tentando seguir de maneira lógica o posicionamento dela referente as matrizes
    # vale comentar que são matrizes 4x4 mas que tem como número inicial (na coordenada (1,1)) o número zero e não um.
    # esse é um padrão do pygame. as matrizes de criação começam no número zero
    types = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[2, 6, 10, 11], [3, 5, 6, 7], [1, 2, 6, 10], [5, 6, 7, 9]],
        [[1, 4, 5, 6], [1, 5, 6, 9], [4, 5, 6, 9], [1, 4, 5, 9]],
        [[1, 2, 5, 6]],
    ]
    # a função construtora da classe de peças do jogo recebe as coordenadas das peças e determina uma cor e tipo para ela 
    # importante comentar que, nesse momento, a imagem ainda não existe, então as funções dessa classe trabalham 
    # apenas com a ideia teórica de como essa imagem se comportará ao ser criada (literalmente gerada) no tabuleiro.
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.types) - 1) # ver se vale a pena mudar pra choice
        self.cor = random.randint(1, len(cores) - 1) # *1 por isso começamos a contagem no segundo elemento da lista 
        self.giro = 0

    # a função update modifica a situação da peça conforme a passagem do tempo gerado dentro do jogo.
    # todo o comportamento da peça se modifica com o tempo. Se não houver movimentação da peça, ou seja, se o jogador
    # não interagir com o jogo no teclado, a peça vai simplesmente cair e "ganhar" posição, indo para a linha de baixo.
    def update(self):
        self.caindo = self.caindo and self.pos_linha > 0
        if self.caindo:
            self.pos_linha -= 1  

    # a função girar simplesmente pega escolhida e gerada (por enquanto apenas teoricamente) e gira ela, sem interferir no 
    # modelo da peça (cor e tipo). ela faz isso percorrendo a lista para garantir que seja um ciclo.
    # o padrão onde a peça começa é a primeira matriz da lista e a função muda ela para a próxima para dar a impressão de
    # ter girado a peça, mas na realidade ele apenas muda a peça para a proxima da lista mantendo a cor selecionada para a anterior
    def girar(self):
        self.giro = (self.giro + 1) % len(self.types[self.type]) #para dar a volta e percorrer a lista toda
    
    # como dito e reforçado na criação dessa classe, as imagens ainda não foram geradas, portanto, por enquanto, não são reais
    # para torná-las reais essa função imagem retorna a peça como uma união do tipo, da cor e da posição para que 
    # não haja dificuldade na geração dela no tabuleiro ou confusão na movimentação dela.
    def imagem(self): # criando uma imagem para tranformar em peça depois
        im = self.types[self.type][self.giro]
        return im
