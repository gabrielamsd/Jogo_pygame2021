#definindo a classe jogo
from peças import *
class Tabuleiro:
    campo = []
    nível = #começa definindo o nível do jogo que aparece na tela, pode ser um único, só determina a dificuldade do jogo
    pontuação = #eu diria que é legal começar do zero
    altura = 20
    largura = 10
    situação = 'start'
    peças = []
    def __init__(self,altura,largura): #Função para criar um campo com tamanho altura x largura
        i = 0 
        k = 0
        while i <= self.altura:
            linha = [] #Criando uma nova linha
            while k <= self.largura :
                linha.append(0) #Espaços vazios serão preenchidos por zero
            self.campo.append(linha) 
    def adiciona_peça(self):
        peça = Peca(10, 10)
        self.peças.append(peça)