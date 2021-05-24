import pygame
from jogo import *
from tamanhocores import *

pygame.init() # começa o jogo (comando do próprio pygame)
jogando = True
dimensão = (400, 700) # testamos algumas combinações, mas, por hora, essa é a mais interessante
tela = pygame.display.set_mode(dimensão)
pygame.display.set_caption('Tetris') # não necessariamente vai chamar assim, mas como é uma tentativa de replicar o tetris original vamos começar testando com esse nome
tabuleiro = Tabuleiro()
while jogando: # formato do handout 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # clicar no x da tela para fechar o jogo
            jogando = False

    tela.fill(CORES['cinza'])
    alt_quadrado = 500/tabuleiro.altura
    lar_quadrado = alt_quadrado
    tela.
    pygame.display.update()