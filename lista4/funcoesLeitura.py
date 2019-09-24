import numpy as np

def lerMatriz(caminhoArquivo):
    """
    Função para ler um arquivo e extrair um matriz de float \n
    @param caminhoArquivo String caminho do arquivo de entrada \n
    @return matriz Matriz de float
    """

    with open(caminhoArquivo) as arq:

        n = int(arq.readline()) # Tamanho de linhas e colunas de uma matriz

        matriz = np.empty((n, n), dtype = float) # Inicializando a matriz com 0's

        for i in range(0, n): # Lendo todas as linhas necessárias para criar a matriz
            
            linha = arq.readline() # Lendo a linha

            aux = linha[0:(len(linha)-1)] # Removendo o \n e os registros separados por espaço
            
            matriz[i] = list(map(float, aux.split(" "))) # Atribuindo os valores da linha na linha da matriz
            
    arq.close()

    return matriz