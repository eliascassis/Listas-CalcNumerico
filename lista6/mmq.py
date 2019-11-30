import numpy as np

# Monta a matriz proposta
def sistema_equacoes_normais(x):
    m = x.size()
    A = np.empty((m, 3), dtype=float)
    for i in range(0, m):
        for j in range(0, 3):
            if(j == 0):
                A[i][j] = 1
            if(j == 1):
                A[i][j] = x[i] 
            if(j == 2):
                A[i][j] = x[i] ** 2
    return A

# Calcula M = AA^T
def m(A):
    return A@np.linalg.transpose(A)

# Calcula F = A^Ty
def f(A, y):
    return np.linalg.transpose(A)@y