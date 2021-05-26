#definindo a classe jogo
from peças import *
import pygame
class Tabuleiro(pygame.sprite.Sprite):
    #nível = #começa definindo o nível do jogo que aparece na tela, pode ser um único, só determina a dificuldade do jogo
    #pontuação = #eu diria que é legal começar do zero
    altura = 20
    largura = 10
    situação = 'start'
    peças = []
    def __init__(self,altura,largura): #Função para criar um campo com tamanho altura x largura
        self.altura = altura 
        self.largura = largura
        
    def adiciona_peça(self):
        peça = Peca(self)
        self.peças.append(peça)

    def update(self):
        pass