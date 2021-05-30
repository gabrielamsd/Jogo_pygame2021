import pygame
from jogo import *
from tamanhocores import *
from peças import *
pygame.init() # começa o jogo (comando do próprio pygame)
pygame.mixer.init()
dimensão = (800, 600) # testamos algumas combinações, mas, por hora, essa é a mais interessante
tela = pygame.display.set_mode(dimensão)
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
jogando = True
clock  = pygame.time.Clock()
FPS = 5
pygame.display.set_caption('Tetris') # não necessariamente vai chamar assim, mas como é uma tentativa de replicar o tetris original vamos começar testando com esse nome
all_sprites = pygame.sprite.Group()
tabuleiro = Tabuleiro(10,20)
ultima_peca = Peca(tabuleiro, tela, pecas[random.choice(list(pecas.keys()))]) 
all_sprites.add(ultima_peca)

while jogando: # formato do handout 
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # clicar no x da tela para fechar o jogo
            jogando = False
    
    if not ultima_peca.caindo:
        ultima_peca = Peca(tabuleiro, tela, pecas[random.choice(list(pecas.keys()))])
        all_sprites.add(ultima_peca)
    
    def mov_lateral(peca, lat):
        pecas.keys = peca
        Peca.rect.x += lat
        if pecas.intersects():
            Peca.rect.x = pecas.keys 
    
           
    
    all_sprites.update()
    tela.fill(CORES['preto'])
    all_sprites.draw(tela)
    
    pygame.display.update()
