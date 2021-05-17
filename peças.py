import pygame
import random
# vamos começar criando as imagens das peças que eu quero usar para a composição do jogo.
# vamos usar, inicialmente, os formatos das peças do jogo original
# para isso, será criada uma classe de peças
class Peças:
    peças = [[[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],[[1, 5, 9, 13], [4, 5, 6, 7]], [[5, 6, 7, 9], [2, 6, 10, 11], [1, 2, 6, 10], [3, 5, 6, 7]],[[1, 4, 5, 9], [4, 5, 6, 9], [1, 4, 5, 6], [1, 5, 6, 9]]]
    def __init__(self):
        self.cor = random.randint(1, len(cores)-1) #randomicamente escolhendo uma cor para a peça
    def rotação(self):
        self.peças[self.type]
    [self.rotação]
    def __init__(self, a, b):
        self.a = a # não temos os tamanhos ainda, mas seria o equivalente a largura
        self.b = b # e altura; tamanho das peças dentro do jogo.
        self.type = random.randint(0, len(self.peças)-1) # esse método de randint com os argumentos foi uma ajuda de um amigo que faz faculdade de design de jogos nos eua. Eu não estava achando no stack como fazer isso e ele me ajudou
# nessa classe as peças do jogo são definidas com valores de posição estilo matriz. 
# cada lista tem a lista principal com a posição padrão da peça seguido pelas variações de posição desse mesmo formato