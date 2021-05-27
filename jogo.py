#definindo a classe jogo
from peças import *
import pygame
class Tabuleiro(pygame.sprite.Sprite):
    #nível = #começa definindo o nível do jogo que aparece na tela, pode ser um único, só determina a dificuldade do jogo
    #pontuação = #eu diria que é legal começar do zero
    altura = 20
    largura = 10
    situação = 'start'
    tabuleiro = []
    peças = []
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

    def colide(self):
        colisao = False 
        for i in range(4):
            for e in range(4):
                if i * 4 + e in Peca.rect.image():
                    if (i + Peca.rect.x > self.altura - 1) or (e + Peca.rect.y < 0) or (self.tabuleiro[i +Peca.rect.x][e + Peca.rect.y]>0) or (e + Peca.rect.y > self.largura - 1):
                        colisao = True
        return colisao
'''
    def para_peca(self):
        for i in range(4):
            for e in range(4):
                if i * 4 + e in Peca.rect.image():
                    self.tabuleiro[i + Peca.rect.x][e + Peca.rect.y] = main.pecas
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "você perdeu :("       
'''
        
