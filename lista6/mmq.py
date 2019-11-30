import numpy as np
import math

def substituicao(A, b):
    """
    Uso: x = substituicao(A,b)    
    Essa funcao resolve o sistema de equacoes lineares Ax=b
    por substituicoes sucessivas, ou seja, assume-se que A
    e uma matriz triangular inferior.
    """
    n = len(b)
    x = np.zeros(n)
    for i in range(n):
        soma = 0
        for j in range(i):
            soma += A[i,j] * x[j]
        x[i] = ( b[i] - soma ) / A[ i, i ]
    
    return np.matrix(x).transpose()	
                    
# -----------------------------------------------------------------------------

def retrosubstituicao(A,b):
    """
    Uso: x = retrosubstituicao(A,b)
    Essa funcao resolve o sistema de equacoes lineares Ax=b
    por substituicoes retroativas, ou seja, assume-se que A
    e uma matriz triangular superior.
    """
    n = len(b)
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        soma = 0
        for j in range(i+1,n):
            soma += A[i,j] * x[j]
        x[i] = (b[i] - soma)/A[i,i]

    return np.matrix(x).transpose()

# -----------------------------------------------------------------------------
	
def cholesky(A):
    """
    Uso: G = cholesky(A)
    
    Essa funcao gera a matriz G da decomposicao de Cholesky
    e a armazena na propria matriz A.
    """
    n = A.shape[0]

    # etapa de eliminacao
    for j in range(0,n):
        soma = 0
        for k in range(0,j):
            soma += A[j,k]*A[j,k]

        try: 
            A[j,j] = math.sqrt( A[j,j] - soma )
        except ValueError:
            print("A matriz nao eh positiva definida.")
                
        for i in range(j+1,n):
            soma = 0
            for k in range(0,j):
                soma += A[i,k]*A[j,k]
            A[i,j] = ( A[i,j] - soma ) / A[j,j]

    # zera a parte triangular superior
    for k in range(1,n):
        A[0:k,k] = 0.0

    return A

# -----------------------------------------------------------------------------

def solveCholesky(G,b):
    """
    Uso: x = choleskySolve(G,b)
    Resolve o sistema Ax=B usando a decomposicao de Cholesky A = G G^T,
    sendo que G foi obtida atraves do uso da funcao cholesky(A) na
    matriz do sistema A.
    
    G deve ser triangular inferior.
    """
    # n = len(b)    
    # substituicao - resolve Gy = b
    y = substituicao(G,b)    
    # retrosubstituicao - resolve G^T x = y
    Gt = G.T
    x = retrosubstituicao(Gt,y)
    return x

# -----------------------------------------------------------------------------

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

# Calcula M = A^T*A
def m(A):
    return np.linalg.transpose(A)@A

# Calcula F = A^Ty
def f(A, y):
    return np.linalg.transpose(A)@y


# Soma dos quadrados dos desvios entre medidas (y) e predições (g(x))
def quadradosMedPred(g, x, y, n):

    soma = 0

    for i in range(0,n):
        soma += (g(x[i]) - y[i])**2

    return soma

def media(y, n):

    soma = 0

    for i in range(0, n):
        soma += y[i]

    return soma/n

# Soma dos quadrados das diferenças em relação à média
def quadradosDifMedia(y, n):

    soma = 0

    ym = media(y, n)

    for i in range(0,n):
        soma += (y[i] - ym)**2

    return soma

def coefDeterminacao(g, x, y, n):

    return 1 - (quadradosMedPred(g, x, y, n) / quadradosDifMedia(y, n))