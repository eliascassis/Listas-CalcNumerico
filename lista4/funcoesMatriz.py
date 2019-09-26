import numpy as np


def substituicao(L, b):
    """
    Aplica o método da substituição \n
    @param L Matriz triangular inferior \n
    @param b vetor com valores desejados \n
    @return x vetor com os valores da solução
    """
    size = b.size()
    x = np.empty(size)
    x[0] = b[0] / L[0][0]
    for i in range(1, size):
        sum = b[i]
        for j in range(1, i - 1):
            sum -= L[i, j] * x[j]
        x[i] = sum / L[i][i]
    return x


def retro_substituicao(U, b):
    """
    Aplica o método da retro-substituição \n
    @param U Matriz triangular superior \n
    @param b vetor com valores desejados \n
    @return x vetor com os valores da solução
    """
    size = b.size()
    x = np.empty(size)
    size -= 1
    x[size] = b[size] / U[size][size]
    for i in range(size-1, 0):
        sum = b[i]
        for j in range(i+1, size):
            sum -= U[i, j] * x[j]
        x[i] = sum / U[i][i]
    return x


def eliminacao_gauss(A, b):
    """
    Aplica o método de gauss \n
    @param L Matriz triangular inferior \n
    @param b vetor com valores desejados \n
    @return x vetor com os valores da solução
    """
    size = b.size()
    for k in range(0, size-1):
        for i in range(k+1, size):
            m = A[i][k] / A[k][k]
            for j in range(k+1, size):
                A[i][j] -= m * A[k][j]
            b[i]-= m * b[k] 
    x = retro_substituicao(A, b)
    return x


def trocarLinhas(A, k, r):
    linhaAux = A[k]
    A[k] = A[r]
    A[r] = linhaAux    


def eliminacao_gauss_pivoteamento(A, b):
    """
    Aplica o método de gauss com pivoteamento\n
    @param L Matriz triangular inferior \n
    @param b vetor com valores desejados \n
    @return x vetor com os valores da solução
    """
    size = b.size()
    for k in range(0, size):
        w = abs(A[k][k])
        for j in range(k, size):
            if abs(A[j][k]) > w:
                w = abs(A[j][k])
                r = j
        trocarLinhas(A, k, r) 
        for i in range(k+1, size):
            m = A[i][k] / A[k][k]
            for j in range(k+1, size):
                A[i][j] -= m * A[k][j]
            b[i]-= m * b[k] 
    x = retro_substituicao(A, b)
    return x
