# dúvidas:
# as peças só vao para a lateral quando passam de uma certa altura do tabuleiro e continuam indo depois de encostar no chão
# tamanho do tabuleiro e as dimensões dele na tela para saber o espaço de jogo
# não conseguimos fazer as colisões
# limites e bordas para o tabuleiro 
import pygame
import random
from tamanhocores import *
pygame.init() # começa o jogo (comando do próprio pygame)
pygame.mixer.init()
dimensão = (700, 700) # testamos algumas combinações, mas, por hora, essa é a mais interessante
tela = pygame.display.set_mode(dimensão)
menu = pygame.image.load('teste.png').convert()#corrigir

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
    'yellow2': pygame.image.load('yellow2.png').convert_alpha(),
    'yellow3': pygame.image.load('yellow3.png').convert_alpha(),
    'yellow4': pygame.image.load('yellow4.png').convert_alpha(),
    'green': pygame.image.load('green.png').convert_alpha(),
    'green2': pygame.image.load('green2.png').convert_alpha(),
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
    def __init__(self, tabuleiro, tela):
        pygame.sprite.Sprite.__init__(self)
        self.tela = tela
        self.tabuleiro = tabuleiro
        self.escolhida = random.choice(list(self.types.values()))
        self.giro = 0 # indica o giro (+1 para direita, -1 para a esquerda) e ve a posição da peça na lista
        self.image = self.escolhida[self.giro]
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_linha = tabuleiro.altura
        self.pos_coluna = tabuleiro.largura/2
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_coluna * 20
        self.rect.y = 0
        self.caindo = True
        self.deslocamento = 0
    def girar(self, orient):
        self.giro += orient
        self.giro = self.giro%len(self.escolhida) #para dar a volta e percorrer a lista toda
        
    def update(self):
        self.caindo = self.caindo and self.pos_linha > 0
        if self.caindo:
            self.pos_linha -= 1  
            self.rect.y += TAM_BLOCO
            self.image = self.escolhida[self.giro] # pegar o elemento, no indice específico do giro, dentro da lista de possiveis posições para a peça em questão.
            self.rect.x += self.deslocamento
'''
        if self.rect.right > self.pos_coluna:
            self.rect.right = self.pos_coluna
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 0:
                self.rect.top = 0 
            if self.rect.bottom > self.pos_linha:
                self.rect.bottom = self.pos_linha
'''
class Tabuleiro(pygame.sprite.Sprite):
    #nível = #começa definindo o nível do jogo que aparece na tela, pode ser um único, só determina a dificuldade do jogo
    #pontuação = #eu diria que é legal começar do zero
    altura = 20
    largura = 10
    situação = 'start'
    tabuleiro = []
    peças = []
    tab = pygame.image.load('tabuleiro.png').convert_alpha()
    def __init__(self,altura,largura): #Função para criar um campo com tamanho altura x largura
        self.altura = altura 
        self.largura = largura
        for i in range(altura):
            cria_linha = []
            for e in range(largura):
                cria_linha.append(0)
            self.tabuleiro.append(cria_linha)

    def adiciona_peça(self):
        peça = Peca(self)
        self.peças.append(peça)

    def update(self):
        pass




# todo: parar a peça no zero ou na colisão
# nessa classe as peças do jogo são definidas com valores de posição estilo matriz. 
# cada lista tem a lista principal com a posição padrão da peça seguido pelas variações de posição desse mesmo formato

jogando = True
clock  = pygame.time.Clock()
FPS = 2
pygame.display.set_caption('Tetris') # não necessariamente vai chamar assim, mas como é uma tentativa de replicar o tetris original vamos começar testando com esse nome
all_sprites = pygame.sprite.Group()
all_blocks = pygame.sprite.Group()
tabuleiro = Tabuleiro(10,20)
ultima_peca = Peca(tabuleiro, tela) 
all_sprites.add(ultima_peca)
while jogando: # formato do handout 
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # clicar no x da tela para fechar o jogo
            jogando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ultima_peca.girar(1)
            if event.key == pygame.K_s:
                ultima_peca.girar(-1)
            if event.key == pygame.K_a:
                ultima_peca.deslocamento = -20
            if event.key == pygame.K_d:
                ultima_peca.deslocamento = +20
        if event.type == pygame.KEYUP: # se não fizer isso vai ficar eternamente somando 1? 
            if event.key == pygame.K_a:
                ultima_peca.deslocamento = 0
            if event.key == pygame.K_d:
                ultima_peca.deslocamento = 0
        
    if not ultima_peca.caindo:
        all_blocks.add(ultima_peca)
        ultima_peca = Peca(tabuleiro, tela)
        all_sprites.add(ultima_peca)
        
    all_sprites.update()
    ultima_peca.rect.y += TAM_BLOCO
  
    hits = pygame.sprite.spritecollide(ultima_peca, all_blocks, False)
    if len(hits) > 0:
        print('colidiu')
        ultima_peca.caindo = False
    ultima_peca.rect.y -= TAM_BLOCO

    tela.fill(CORES['azul'])
    tela.blit(menu, (0,0))
    all_sprites.draw(tela)
    pygame.display.update()
