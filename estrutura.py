import pygame
import random
from tamanhocores import *
from pecas import *
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