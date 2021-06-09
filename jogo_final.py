# importando as bibliotecas
import pygame
import random
from tamanhocores import *
from pecas import *
from estrutura import *
# começando o jogo, determinando as dimensões e a tela do jogo
pygame.init() 
pygame.mixer.init()
dimensão = (500, 600)
tela = pygame.display.set_mode(dimensão)
pygame.display.set_caption("Tetris")
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

while jogando:
    if tabuleiro.peca is None: # cria uma peça quando não existe nenhuma que não esteja ja colidida
        tabuleiro.adiciona_peca()
    # administrando o placar:
    pontos += 1
    if pontos > 999:
        pontos = 0
    if pontos % (FPS // tabuleiro.level // 2) == 0: # vi um indiano no youtube fazendo isso numa réplica de mario. dessa forma o fps não modifica a velocidade de caimento das peças, só a velocidade de reação ao clique
        if tabuleiro.state == "start": # funcionou, porém não entendi
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
                tabuleiro.rodar()
            if event.key == pygame.K_a:
                tabuleiro.deslocamento(-1)
            if event.key == pygame.K_d:
                tabuleiro.deslocamento(1) 

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
    formato = pygame.font.SysFont('Arial', 20, True, False)
    tit = pygame.font.SysFont('Arial', 40, True, False)
    subtexto = pygame.font.SysFont('Arial', 11, True, False)

    # criando as posições onde cada coisa estará escrita
    pos_titulo = [100, 10]
    pos_ponto = [350, 300]
    pos_go = [335, 350] #posição de onde aparece mensagem indicando game over
    pos_nomes = [230, 580]
    # colocar as instruções na lateral !!!!!!!

    # escolhendo o que será escrito
    # frases como autoras do jogo, modo de jogar (quais peças apertar), pontuação e avisar quando a pessoa perder
    titulo = tit.render('TETRIS', True, CORES['verde'])
    texto1 = formato.render('Pontos: ' + str(tabuleiro.pontos), True, CORES['roxo'])
    texto2 = formato.render('Você perdeu!', True, CORES['rosa'])
    texto3 = subtexto.render('Jogo feito por Gabriela e Kailany', True, CORES['azul']) # devemos colocar sobrenomes?
    
    # escrevendo na tela
    tela.blit(titulo, pos_titulo)
    tela.blit(texto3, pos_nomes)
    tela.blit(texto1, pos_ponto)
    if tabuleiro.state == 'fim de jogo':
        tela.blit(texto2, pos_go) 

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()