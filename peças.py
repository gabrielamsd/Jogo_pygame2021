import pygame
import random
from tamanhocores import *
# vamos começar criando as imagens das peças que eu quero usar para a composição do jogo.
# vamos usar, inicialmente, os formatos das peças do jogo original
# para isso, será criada uma classe de peças
class Peca(pygame.sprite.Sprite):
    types = {
        1: [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        2: [[1, 5, 9, 13], [4, 5, 6, 7]],
        3: [[5, 6, 7, 9], [2, 6, 10, 11], [1, 2, 6, 10], [3, 5, 6, 7]],
        4: [[1, 4, 5, 9], [4, 5, 6, 9], [1, 4, 5, 6], [1, 5, 6, 9]]
    }    

    pos_linha = 20 #posição da linha em que a peça começa
    pos_coluna = 1 #posição da coluna em que a peça começa
    rot = 0 #rotaão da peça, começa do zero
    type = []
    def __init__(self, tabuleiro, tela, image):
        pygame.sprite.Sprite.__init__(self)
        self.tela = tela
        self.tabuleiro = tabuleiro
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_linha = tabuleiro.altura
        self.pos_coluna = tabuleiro.largura/2
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_coluna * TAM_BLOCO
        self.rect.y = 0
        self.caindo = True
        self.type = random.choice(list(self.types.values())) # esse método de randint com os argumentos foi uma ajuda de um amigo que faz faculdade de design de jogos nos eua. Eu não estava achando no stack como fazer isso e ele me ajudou
    def rotação(self):
        self.rot = (self.rot + 1) % len(self.type) 
    def update(self):
        self.caindo = self.caindo and self.pos_linha > 0
        if self.caindo:
            self.pos_linha -= 1  
            self.rect.y += TAM_BLOCO
        
# todo: parar a peça no zero ou na colisão
# nessa classe as peças do jogo são definidas com valores de posição estilo matriz. 
# cada lista tem a lista principal com a posição padrão da peça seguido pelas variações de posição desse mesmo formato