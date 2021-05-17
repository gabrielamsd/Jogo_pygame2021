# teste de tamanhos para o jogo:
import pygame
pygame.init() # começa o jogo (comando do próprio pygame)
jogando = True
dimensão = (400, 700) # testamos algumas combinações, mas, por hora, essa é a mais interessante
tela = pygame.display.set_mode(dimensão)
pygame.display.set_caption('Tetris') # não necessariamente vai chamar assim, mas como é uma tentativa de replicar o tetris original vamos começar testando com esse nome

#definindo cores:
preto = (0,0,0)
rosa = (255, 0, 255)
roxo = (151, 50, 151)
vermelho = (255, 0, 0)
amarelo = (255, 215, 50)
verde = (0, 255, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)
cinza = (130, 130, 130)

while jogando: # formato do handout 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # clicar no x da tela para fechar o jogo
            jogando = False

    tela.fill(cinza)
    pygame.display.update()





