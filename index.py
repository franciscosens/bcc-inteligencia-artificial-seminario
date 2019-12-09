import matplotlib.pyplot as plt
from random import randint
import numpy as np

class Seminario:

    STATUS_PENDENTE_MAPEAMENTO = -1
    STATUS_LIVRE_FECHADO = 2
    STATUS_LIVRE = 0 
    STATUS_MINA = 1
    QUANTIDADE_MAXIMA_MINAS = 20
    QUANTIDADE_MINIMA_MINAS = 7

    def __init__(self, linhas, colunas):
        self.pontos_encontrados = []
        self.apresentou = False
        self.quantidade_pontos_para_visitar = 0
        self.lista_visitados = []
        self.navio_linha = 0
        self.navio_coluna = 0
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = []
        self.matriz_mapeada = []
        self.gerar_matriz()
        self.gerar_minas()
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
        self.quantidade_pontos_para_visitar = (self.linhas * self.colunas) - quantidade_minas
        print(quantidade_minas)
        for i in range(0, quantidade_minas):
            posicao_linha = randint(0, len(self.matriz) - 1)
            posicao_coluna = randint(0, len(self.matriz[0]) - 1)
            self.matriz[posicao_linha][posicao_coluna] = self.STATUS_MINA

    def mapear(self):
        y = np.array(self.matriz_mapeada)
        quantidade_elementos = np.count_nonzero(y == -1)
        if(quantidade_elementos == 0):

            if not self.apresentou:
                self.apresentou = True
                for i in range(0, self.linhas):
                    for j in range(0, self.colunas):
                        if self.matriz_mapeada[i][j] == self.STATUS_MINA:
                            self.pontos_encontrados.append([i, j])
                            print(f'{i}x{j}')
            return

        linha = self.navio_linha
        coluna = self.navio_coluna
        if linha + 1 < len(self.matriz) and self.matriz_mapeada[linha + 1][coluna] == self.STATUS_PENDENTE_MAPEAMENTO:
            linha = linha + 1
        elif coluna + 1 < len(self.matriz[0]) and self.matriz_mapeada[linha][coluna + 1] == self.STATUS_PENDENTE_MAPEAMENTO:
            coluna = coluna + 1
        elif self.navio_coluna - 1 >= 0 and coluna - 1 < len(self.matriz[0]) and self.matriz_mapeada[linha][coluna - 1] == self.STATUS_PENDENTE_MAPEAMENTO:
            coluna = coluna - 1
        elif self.navio_linha - 1 >= 0 and linha - 1 < len(self.matriz) and self.matriz_mapeada[linha - 1][coluna] == self.STATUS_PENDENTE_MAPEAMENTO:
            linha = linha - 1

        self.descobrir_minas()

        if linha == self.navio_linha and coluna == self.navio_coluna:
            if len(self.lista_visitados) > 0:
                visitado = self.lista_visitados.pop()
                self.navio_linha = visitado[0]        
                self.navio_coluna = visitado[1]        
        elif self.matriz[linha][coluna] == self.STATUS_MINA:
            self.matriz_mapeada[linha][coluna] = self.STATUS_MINA
        elif self.matriz_mapeada[linha][coluna] == self.STATUS_PENDENTE_MAPEAMENTO:
            self.matriz_mapeada[linha][coluna] = self.STATUS_LIVRE
            self.navio_coluna = coluna
            self.navio_linha = linha
            self.lista_visitados.append([linha, coluna])
        elif self.matriz_mapeada[linha][coluna] == self.STATUS_LIVRE:
            self.matriz_mapeada[linha][coluna] = self.STATUS_LIVRE_FECHADO
            self.navio_coluna = coluna
            self.navio_linha = linha
            self.lista_visitados.append([linha, coluna])
        # self.apresentar_matriz(self.matriz_mapeada)

    def descobrir_minas(self):
        if self.navio_linha + 1 < len(self.matriz) and self.matriz[self.navio_linha + 1][self.navio_coluna] == self.STATUS_MINA:
            self.matriz_mapeada[self.navio_linha + 1][self.navio_coluna] = self.STATUS_MINA

        if self.navio_coluna + 1 < len(self.matriz[0]) and self.matriz[self.navio_linha][self.navio_coluna + 1] == self.STATUS_MINA:
            self.matriz_mapeada[self.navio_linha][self.navio_coluna + 1] = self.STATUS_MINA

        if self.navio_coluna - 1 >= 0 and self.navio_coluna - 1 < len(self.matriz[0]) and self.matriz[self.navio_linha][self.navio_coluna - 1] == self.STATUS_MINA:
            self.matriz_mapeada[self.navio_linha][self.navio_coluna - 1] = self.STATUS_MINA

        if self.navio_linha - 1 >= 0 and self.navio_linha - 1 < len(self.matriz) and self.matriz[self.navio_linha - 1][self.navio_coluna] == self.STATUS_MINA:
            self.matriz_mapeada[self.navio_linha - 1][self.navio_coluna] = self.STATUS_MINA


    def exibir(self):
        fig, (ax1, ax2) = plt.subplots(1, 2)
        plt.show(block=False)
        while 1 == 1:
            ax1.imshow(self.matriz, 'Blues')
            ax1.plot(self.navio_coluna, self.navio_linha, '*r', 'Oceano', 5)

            ax2.imshow(self.matriz_mapeada, 'Dark2')
            ax2.plot(self.navio_coluna, self.navio_linha, '*r', 'Bombas mapeadas', 5)
            plt.pause(0.01)
            self.mapear()
            ax1.cla()
            ax2.cla()
            
    def apresentar_matriz(self, matriz):
        print("--------------------------------------------------------------------------------------------")
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[i])):
                print(str(self.matriz[i][j]) + " ", end="")
            print()

if __name__ == "__main__":
    q = Seminario(20, 20)
