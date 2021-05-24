import pygame
import random
from tamanhocores import *
# vamos começar criando as imagens das peças que eu quero usar para a composição do jogo.
# vamos usar, inicialmente, os formatos das peças do jogo original
# para isso, será criada uma classe de peças
class Peca:
    types = {
        1: [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        2: [[1, 5, 9, 13], [4, 5, 6, 7]],
        3: [[5, 6, 7, 9], [2, 6, 10, 11], [1, 2, 6, 10], [3, 5, 6, 7]],
        4: [[1, 4, 5, 9], [4, 5, 6, 9], [1, 4, 5, 6], [1, 5, 6, 9]]
    }    
    posição = 0   
    type = []
    def __init__(self, a, b):
        self.a = 10 # não temos os tamanhos ainda, mas seria o equivalente a largura
        self.b = 10 # e altura; tamanho das peças dentro do jogo.
        self.type = random.choice(list(self.types.values())) # esse método de randint com os argumentos foi uma ajuda de um amigo que faz faculdade de design de jogos nos eua. Eu não estava achando no stack como fazer isso e ele me ajudou
        self.cor = random.choice(list(CORES.keys()))
    def rotação(self):
        self.posição = (self.posição + 1) % len(self.type) 
# nessa classe as peças do jogo são definidas com valores de posição estilo matriz. 
# cada lista tem a lista principal com a posição padrão da peça seguido pelas variações de posição desse mesmo formato