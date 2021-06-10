# importando as bibliotecas
import pygame
import random
from cores import *
from pecas import *
from estrutura import *
# começando o jogo, determinando as dimensões e a tela do jogo
pygame.init() 
pygame.mixer.init()
dimensão = (500, 600)
tela = pygame.display.set_mode(dimensão)
pygame.display.set_caption("Tetris")

# tela de início
# ecolhemos um design com o título do jogo em destaque e o resto meio borrado para remeter ao vintage do jogo original
inicio_img = pygame.image.load(path.join('telainicio.png'))

# enquanto estiver jogando, ele vai rodar no loop
jogando = True 

clock = pygame.time.Clock()
FPS = 40
matriz = 4
tabuleiro = Tabuleiro(25, 12)
pontos = 0
# criando variáveis para organizar o código
a =  tabuleiro.amp - 2
b = tabuleiro.amp - 1
c = tabuleiro.amp
d = tabuleiro.x
aa = tabuleiro.y
deixa_cair = False
tela_inicio = False

# música do jogo original (perdão direito autorais)
pygame.mixer.music.load((path.join('musica_tetris.mp3')))
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.2)

#preencher a tela com a tela inicial
while tela_inicio == False:
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            tela_inicio = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tela_inicio = True
 
    tela.fill(CORES['preto'])
    inicio = pygame.image.load('telainicio.png')
    inicio = pygame.transform.scale(inicio, (500, 600))
    tela.blit(inicio,(0,0))
    pygame.display.flip()


while jogando:
    # cria uma peça quando não existe nenhuma que não esteja ja colidida
    if tabuleiro.peca is None: 
        tabuleiro.adiciona_peca()
    # administrando o placar:
    # o placar começa no zero e vai até 999, na pontuação '1000' ele zera
    pontos += 1
    if pontos > 999:
        pontos = 0
    # garante que o tempo da peça caindo não mude com o fps e sim com um valor padrão determinado na biblioteca Tabuleiro
    if pontos % (FPS // tabuleiro.padrão // 2) == 0: 
        if tabuleiro.state == "start": 
            tabuleiro.cai()
    # deixa a peça cair quando aperta para baixo
    if deixa_cair:
        if tabuleiro.state == "start": 
            tabuleiro.cai()

    #colore a tela (a cor é opcional, mas preto é a que ficou esteticamente mais bonita)
    tela.fill(CORES['preto']) 

    # eventos de teclado, o que cada tecla faz 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            jogando = False # modelo de fechar o jogo clicando no x da tela
        if event.type == pygame.KEYDOWN: # o jogo funciona com as teclas wasd
            if event.key == pygame.K_w:
                tabuleiro.rodar()
            if event.key == pygame.K_s:
                deixa_cair = True
            if event.key == pygame.K_UP: # e com as setas do teclado
                tabuleiro.rodar()
            if event.key == pygame.K_DOWN:
                deixa_cair = True
            if event.key == pygame.K_a:
                tabuleiro.deslocamento(-1)
            if event.key == pygame.K_d:
                tabuleiro.deslocamento(1)
            if event.key == pygame.K_LEFT:
                tabuleiro.deslocamento(-1)
            if event.key == pygame.K_RIGHT:
                tabuleiro.deslocamento(1)
        if event.type == pygame.KEYUP: # faz parar de cair para não afetar as outras peças
            if event.key == pygame.K_s:
                deixa_cair = False
            if event.key == pygame.K_DOWN:
                deixa_cair = False


    # desenhando a grade quadriculada que é o espaço de jogo
    for i in range(tabuleiro.altura):
        for e in range(tabuleiro.largura):
            pygame.draw.rect(tela,CORES['branco'], [d + c * e, aa + c * i, c, c], 1)
            if tabuleiro.campo[i][e] > 0:
                pygame.draw.rect(tela, cores[tabuleiro.campo[i][e]],[d + c * e + 1, aa + c * i + 1, a, b])
    # desenhando as peças com os comandos do próprio pygame        
    # transformando as coordenadas matriciais em algo mais real                      
    if tabuleiro.peca is not None: 
        for i in range(matriz):
            for e in range(matriz):
                if (i * matriz + e) in tabuleiro.peca.imagem():
                    pygame.draw.rect(tela, cores[tabuleiro.peca.cor], [d + c * (e + tabuleiro.peca.x) + 1, aa + c * (i + tabuleiro.peca.y) + 1, a, a])

    # escrevendo na tela:
    # determinando os formatos da fonte e tamanho de cada texto utilizado
    formato = pygame.font.SysFont('Arial', 35, True, False)
    tit = pygame.font.SysFont('Arial', 40, True, False)
    subtexto = pygame.font.SysFont('Arial', 11, True, False)
    subtexto1 = pygame.font.SysFont('Arial', 15, True, False)

    # criando as posições onde cada coisa estará escrita
    pos_titulo = [100, 10]
    pos_ponto = [310, 10]
    pos_go = [300, 260] #posição de onde aparece mensagem indicando game over
    pos_nomes = [230, 580]
    pos_i1 = [300, 110]
    pos_i2 = [300, 125]
    pos_i3 = [300, 140]
    pos_i4 = [300, 155]
    pos_i5 = [300, 170]
    pos_i6 = [300, 185]

    # escolhendo o que será escrito
    # frases como autoras do jogo, modo de jogar (quais peças apertar), pontuação e avisar quando a pessoa perder
    titulo = tit.render('TETRIS', True, CORES['laranja'])
    texto1 = formato.render('Pontos: ' + str(tabuleiro.pontos), True, CORES['roxo'])
    texto2 = formato.render('Gameover!', True, CORES['rosa'])
    texto3 = subtexto.render('Jogo feito por Gabriela Duarte e Kailany Kellen', True, CORES['azul']) 
    # textos de instrução na tela de jogo
    textoi1 = subtexto1.render('Para mover a peça', True, CORES['rosinha'])
    textoi2 = subtexto1.render('lateralmente aperte', True, CORES['rosinha'])
    textoi3 = subtexto1.render('A e D ou ← e →', True, CORES['rosinha'])
    textoi4 = subtexto1.render('Para girar use as', True, CORES['rosinha'])
    textoi5 = subtexto1.render('teclas W ou ↑ ', True, CORES['rosinha'])
    textoi6 = subtexto1.render('Dica: S e ↓ aceleram a queda', True, CORES['rosinha'])
    

    # escrevendo na tela
    tela.blit(titulo, pos_titulo)
    tela.blit(texto3, pos_nomes)
    tela.blit(texto1, pos_ponto)
    tela.blit(textoi1, pos_i1)
    tela.blit(textoi2, pos_i2)
    tela.blit(textoi3, pos_i3)
    tela.blit(textoi4, pos_i4)
    tela.blit(textoi5, pos_i5)
    tela.blit(textoi6, pos_i6)

    if tabuleiro.state == 'fim de jogo':
        tela.blit(texto2, pos_go) 

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()