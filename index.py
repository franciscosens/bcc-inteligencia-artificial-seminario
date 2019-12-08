import matplotlib.pyplot as plt
from random import randint

class Seminario:

    STATUS_PENDENTE_MAPEAMENTO = -1
    STATUS_LIVRE = 0 
    STATUS_MINA = 1
    QUANTIDADE_MAXIMA_MINAS = 10
    QUANTIDADE_MINIMA_MINAS = 7

    def __init__(self, linhas, colunas):
        self.navio_linha = 0
        self.navio_coluna = 0
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = []
        self.matriz_mapeada = []
        self.gerar_matriz()
        self.gerar_minas()
        # self.apresentar_matriz()
        self.exibir()

    def gerar_matriz(self):
        for i in range(0, self.linhas):
            linha = []
            linha_mapeamento = []
            for j in range(0, self.colunas):
                linha.append(0)
                linha_mapeamento.append(self.STATUS_PENDENTE_MAPEAMENTO)
            self.matriz.append(linha)
            self.matriz_mapeada.append(linha_mapeamento)

    def gerar_minas(self):
        quantidade_minas = randint(self.QUANTIDADE_MAXIMA_MINAS, self.QUANTIDADE_MAXIMA_MINAS)
        print(quantidade_minas)
        for i in range(0, quantidade_minas):
            posicao_linha = randint(0, len(self.matriz) - 1)
            posicao_coluna = randint(0, len(self.matriz[0]) - 1)
            self.matriz[posicao_linha][posicao_coluna] = self.STATUS_MINA

    def mapear(self):
        linha = self.navio_linha
        coluna = self.navio_coluna
        if linha + 1 < len(self.matriz) and self.matriz_mapeada[linha + 1][coluna] == self.STATUS_PENDENTE_MAPEAMENTO:
            linha = linha + 1
            if self.matriz[linha][coluna] == self.STATUS_MINA:
                self.matriz_mapeada[linha][coluna] = self.STATUS_MINA
            else:
                self.matriz_mapeada[linha][coluna] = self.STATUS_LIVRE
                self.navio_linha = linha
        elif coluna + 1 < len(self.matriz[0]) and self.matriz_mapeada[linha][coluna+1] == self.STATUS_PENDENTE_MAPEAMENTO:
            coluna = coluna + 1
            if self.matriz[linha][coluna] == self.STATUS_MINA:
                self.matriz_mapeada[linha][coluna] = self.STATUS_MINA
            else:
                self.matriz_mapeada[linha][coluna] = self.STATUS_LIVRE
                self.navio_coluna = coluna
        elif  coluna - 1 < len(self.matriz[0]) and self.matriz_mapeada[linha][coluna - 1] == self.STATUS_PENDENTE_MAPEAMENTO:
            coluna = coluna - 1
            if self.matriz[linha][coluna] == self.STATUS_MINA:
                self.matriz_mapeada[linha][coluna] = self.STATUS_MINA
            else:
                self.matriz_mapeada[linha][coluna] = self.STATUS_LIVRE
                self.navio_coluna = coluna
        # self.apresentar_matriz(self.matriz_mapeada)
        
        # self.navio_coluna = self.navio_coluna + 1

    def exibir(self):
        while 1 == 1:
            plt.imshow(self.matriz, 'Blues')
            plt.show(block=False)
            plt.plot(self.navio_coluna, self.navio_linha, '*r', 'LineWidth', 5)
            plt.pause(0.1)
            self.mapear()
            plt.clf()

    def apresentar_matriz(self, matriz):
        print("--------------------------------------------------------------------------------------------")
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[i])):
                print(str(self.matriz[i][j]) + " ", end="")
            print()

if __name__ == "__main__":
    q = Seminario(10, 10)
