import numpy as np

def sistema_equacoes_normais(pontos):
    m = pontos.size()
    A = np.empty((m, 3), dtype=float)
    for i in range(0, m):
        for j in range(0, 3):
            if(j == 0):
                A[i][j] = 1
            if(j == 1):
                A[i][j] = pontos[0] 
            if(j == 2):
                A[i][j] = pontos[0] ** 2

# Calcula M = AA^T
def m(A):
    return A@np.linalg.transpose(A)

# Calcula F = A^Ty
def f(A, y):
    return np.linalg.transpose(A)@y