#definindo a classe jogo
class tabuleiro:
    campo = []
    nível = #começa definindo o nível do jogo que aparece na tela, pode ser um único, só determina a dificuldade do jogo
    pontuação = #eu diria que é legal começar do zero
    altura = x
    largura = y
    situação = 'start'
    def __init__(self,altura,largura): #Função para criar um campo com tamanho altura x largura
        i = 0 
        k = 0
        while i <= self.altura:
            linha = [] #Criando uma nova linha
            while k <= self.largura :
                linha.append(0) #Espaços vazios serão preenchidos por zero
            self.campo.append(linha) 