from tamanhocores import * 
import pygame
import random

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
