# importando as bibliotecas
import pygame
import random
from tamanhocores import *
# começando o jogo, determinando as dimensões e a tela do jogo
pygame.init() 
pygame.mixer.init()
dimensão = (500, 600)
tela = pygame.display.set_mode(dimensão)

# lista de cores para que as peças sejam de cores aleatórias. o comando random escolhe uma cor da lista e pinta o formato da peça com ela
cores = [
    CORES['laranja'],
    CORES['azul'],
    CORES['verde'],
    CORES['verdao'],
    CORES['rosinha'],
    CORES['roxo'] 
]

class Peca:
    # nessa classe as peças do jogo são definidas com valores de posição estilo matriz. 
    # cada lista tem a lista principal com a posição padrão da peça seguido pelas variações de posição desse mesmo formato

    types = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [2, 6, 10, 11], [5, 6, 7, 9], [3, 5, 6, 7]],
        [[1, 4, 5, 6],[4, 5, 6, 9], [1, 4, 5, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.types) - 1) # ver se vale a pena mudar pra choice
        self.cor = random.randint(1, len(cores) - 1)
        self.giro = 0

    def update(self):
        self.caindo = self.caindo and self.pos_linha > 0
        if self.caindo:
            self.pos_linha -= 1  
            self.rect.y += TAM_BLOCO
            self.imagem = self.escolhida[self.giro] # pegar o elemento, no indice específico do giro, dentro da lista de possiveis posições para a peça em questão.
            self.rect.x += self.deslocamento

    def girar(self):
        self.giro = (self.giro + 1) % len(self.types[self.type]) #para dar a volta e percorrer a lista toda
    
    def imagem(self): # criando uma imagem para tranformar em peça depois
        return self.types[self.type][self.giro]


class Tabuleiro:
    level = 2
    pontos = 0
    state = "start"
    campo = []
    # as matrizes criadoras dos elementos peça são 4x4. caso queiramos mudar o tamanho, podemos alterar diretamente aqui ao inves de usar 4 sempre
    matriz = 4 
    x = 50
    y = 60
    amp = 20
    peca = None

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
        self.campo = []
        self.pontos = 0
        self.state = "start"
        for i in range(altura):
            mais_linha = []
            for e in range(largura):
                mais_linha.append(0)
            self.campo.append(mais_linha)

    def adiciona_peca(self):
        # queremos que a peca comece a cair de cima e no centro do tabuleiro
        # portanto no eixo x, queremos 4 e no y 0
        self.peca = Peca(4, 0) # posição que a peça aparece no tabuleiro

    # função que faz a peça rodar (mudar a posição em torno dela mesma) a partir das coordenadas matriciais
    def rodar(self):
        roda = self.peca.giro
        self.peca.girar()
        if self.colisao(self.peca.y, self.peca.x):
            self.peca.giro = roda
    
    # a função deslocamento, abaixo, mexe a peça para a esquerda e para a direita. no loop é possível determinar as teclas
    # que regem esse movimento. ela também verifica a colisão com as paredes 
    def deslocamento(self, dx):
        pos_anterior = self.peca.x
        self.peca.x += dx
        if self.colisao(self.peca.y, self.peca.x):
            self.peca.x = pos_anterior
    
    # como ver se uma peça bate na outra? precisamos trabalhar em função das matrizes, já que não sao imagens reais
    # mas só consideramos as coordenadas preenchidas para colidir as peças. caso contrário todas seriam peças 4x4
    def colisao(self, ay, ax):
        matriz = 4
        self.peca.y = ay
        self.peca.x = ax
        colide = False
        for i in range(matriz):
            for e in range(matriz):
                if (i * matriz + e) in self.peca.imagem():
                    if (i + ay > self.altura - 1) or (e + ax > self.largura - 1) or (e + ax < 0) or (self.campo[i + ay][e + ax] > 0):
                        colide = True
        return colide

    # a função abaixo verifica se houve colisão das peças e, uma vez que houve, usa outras funções para determinar se ainda 
    # tem espaço para criar novas peças. Se não tiver, é a situação em que o jogo acaba e o jogador perde. 
    # Já aproveitamos então para definir a situação de fim de jogo quando isso acontece.
    # com isso, no loop a gente consegue criar as frases indicando que o jogo acabou e impedimos a criação de mais peças.
    def colidiu(self, matriz):
        for i in range(matriz):
            for e in range(matriz):
                if (i * matriz + e) in self.peca.imagem():
                    (self.campo[i + self.peca.y][e + self.peca.x]) = self.peca.cor
        self.pontua()
        self.adiciona_peca()
        if self.colisao(self.peca.y, self.peca.x):
            self.state = "fim de jogo"

    # verificamos, na função abaixo, a quebra de linhas. no jogo Tetris original, quando uma linha inteira é preenchida ela é apagada
    # essa quebra de linhas é o que da pontos para o jogador. na nossa versão não poderia ser diferente 
    def pontua(self):
        linha = 0
        for i in range(1, self.altura):
            esp_vazio = 0
            for k in range(self.largura):
                if self.campo[i][k] == 0:
                    esp_vazio += 1
            if esp_vazio == 0:
                linha += 1
                for e in range(i, 1, -1):
                    for k in range(self.largura):
                        self.campo[e][k] = self.campo[e - 1][k]
        self.pontos += linha ** 2
    # os pontos obtidos por cada quebra de linha são referentes a quantidade de linhas quebradas por vez. se uma linha foi preenchida,
    # o jogador ganha 1 ponto, mas se mais de uma linha por vez é preenchida, o ganho é exponencial. Assim, quebrando 2 linhas
    # a pontuação sobe para 2 por linha, ou seja, 4 pontos. Com 3 linhas preenchidas ao mesmo tempo, cada linha vale 3 e, potanto, o 
    # jogador pontua 9 pontos de uma vez só.

    # essa é a função que cria gravidade no jogo e faz a peça cair de quadradinho por quadradinho, sem meio termo.
    # a ideia disso é imitar o jogo original, que tinha uma velocidade mais baixo e, portanto, não conseguia simular com precisão a 
    # queda das peças. Além disso, a função cai ja aproveita para ver a colisão e verifica se as peças colidiram tanto com outras peças
    # como com o tabuleiro e faz elas pararem de cair quando a colisão é identificada.
    def cai(self):
        matriz = 4
        self.peca.y += 1
        if self.colisao(self.peca.y, self.peca.x):
            self.peca.y -= 1
            self.colidiu(matriz)



pygame.display.set_caption("Tetris")
jogando = True # enquanto estiver jogando, ele vai rodar no loop
clock = pygame.time.Clock()
FPS = 10
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