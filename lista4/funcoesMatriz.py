import numpy as np


def replacement(L, b):
    size = b.size()
    x = np.empty(size)
    x[0] = b[0] / L[0][0]
    for i in range(1, size):
        sum = b[i]
        for j in range(1, i - 1):
            sum -= L[i, j] * x[j]
        x[i] = sum / L[i][i]
    return x


def re_replacement(U, b):
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


def gauss_elimination(A, b):
    size = b.size()
    for k in range(0, size-1):
        for i in range(k+1, size):
            m = A[i][k] / A[k][k]
            for j in range(k+1, size):
                A[i][j] -= m * A[k][j]
            b[i]-= m * b[k] 
    x = re_replacement(A, b)
    return x

