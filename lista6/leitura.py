import numpy as np

def leitura(caminhoArquivo):
    """
    Função para ler um arquivo e extrair os vetores com x's e y's \n
    @param caminhoArquivo String caminho do arquivo de entrada \n
    @return pair<x,y> vetores x e y
    """

    with open(caminhoArquivo, 'r') as arq:

        # contadores auxiliares para os vetores
        n = 0
        i = 0

        # Tamanho do conjunto de pares
        for linha in arq:
            n += 1

        arq.seek(0) # Voltando ao inicio do arquivo 

        x = np.zeros(n, dtype=float)
        y = np.zeros(n, dtype=float)

        for linha in arq: 
            
            par = linha.split(";") # Criando um vetor par com x e y

            x[i] = par[0]
            y[i] = par[1]

            i+=1
                        
    arq.close()

    return x, y