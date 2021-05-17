import pygame
# vamos começar criando as imagens das peças que eu quero usar para a composição do jogo.
# vamos usar, inicialmente, os formatos das peças do jogo original
# para isso, será criada uma classe de peças
class Peças:
    peças = [[[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],[[1, 5, 9, 13], [4, 5, 6, 7]], [[5, 6, 7, 9], [2, 6, 10, 11], [1, 2, 6, 10], [3, 5, 6, 7]],[[1, 4, 5, 9], [4, 5, 6, 9], [1, 4, 5, 6], [1, 5, 6, 9]]]
# nessa classe as peças do jogo são definidas com valores de posição estilo matriz. 
# cada lista tem a lista principal com a posição padrão da peça seguido pelas variações de posição desse mesmo formato