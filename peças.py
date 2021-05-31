import pygame
import random
from tamanhocores import *
# vamos começar criando as imagens das peças que eu quero usar para a composição do jogo.
# vamos usar, inicialmente, os formatos das peças do jogo original
pecas = {
    'red': pygame.image.load('red.png').convert_alpha(),
    'blue': pygame.image.load('blue.png').convert_alpha(),
    'blue2': pygame.image.load('blue2.png').convert_alpha(),
    'blue3': pygame.image.load('blue3.png').convert_alpha(),
    'blue4': pygame.image.load('blue4.png').convert_alpha(),
    'purple': pygame.image.load('purple.png').convert_alpha(),
    'purple2': pygame.image.load('purple2.png').convert_alpha(),
    'purple3': pygame.image.load('purple3.png').convert_alpha(),
    'purple4': pygame.image.load('purple4.png').convert_alpha(),
    'yellow': pygame.image.load('yellow.png').convert_alpha(),
    'green': pygame.image.load('green.png').convert_alpha(),
    'pink': pygame.image.load('pink.png').convert_alpha(),
    'pink2': pygame.image.load('pink2.png').convert_alpha(),
    'cyan': pygame.image.load('cyan.png').convert_alpha(),
    
}
# para isso, será criada uma classe de peças
class Peca(pygame.sprite.Sprite):
    types = {
        1: [pecas['pink'], pecas['pink2']],
        2: [pecas['blue'],pecas['blue2'],pecas['blue3'],pecas['blue4']],
        3: [pecas['purple'], pecas['purple2'], pecas['purple3'], pecas['purple4']],
        4: [pecas['yellow'], pecas['yellow2'], pecas['yellow3'], pecas['yellow4']],
        5: [pecas['red']],
        6: [pecas['green'], pecas['green2']],
        7: [pecas['cyan']]
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