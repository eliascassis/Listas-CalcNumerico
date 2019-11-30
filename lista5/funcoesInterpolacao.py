import numpy as np
import math
#from lista4 import funcoesMatriz as fM

def decompLU(A):
    """
    Uso: decompLU(A)
    
    Essa funcao decompoe a matriz de coeficientes A no produto LU
    e armazena o resultado na propria matriz A.
    """
    n = A.shape[ 0 ]
    # Etapa de eliminacao
    for k in range(0,n-1):
        for i in range(k+1,n):
            if A[i,k] != 0.0:
                m = A[i,k]/A[k,k]
                A[i,k] = m
                for j in range(k+1,n):
                    A[i,j] = A[i, j] - m * A[k,j]

# -----------------------------------------------------------------------------

def solveLU(A,b):    
    """
    Uso: x = solveLU(A,b)
    Essa funcao recebe uma matriz A = LU, a qual ja foi fatorada
    em L e U e resolve o sistemas de equacoes y = np.zeros(n)Ax = b e retorna
    o vetor solucao x.
    
    Etapas:
      - a matriz A deve ser [A]=[L/U]
      - b eh o vetor do lado direito
      - resolve Ly = b
      - resolve Ux = y
      - retorna a solucao em x
    """
    n = len(A)
    x = np.zeros(n, dtype=float)
    y = np.zeros(n, dtype=float)
    
    # substituicao
    y[0] = b[0]
    for k in range(1,n):
        y[k] = b[k] - np.dot(A[k,0:k], y[0:k])

    # retrosubstituicao
    for k in range(n-1,-1,-1):
        x[k] = (y[k] - np.dot(A[k,k+1:n],x[k+1:n]))/A[k,k]

    return x

def f(x):
    """
    f(x) = 1/(1 + 25*(x**2))
    """
    return 1/(1 + 25*(x**2))

def pontos(n):
    """
    Função para retornar um vetor com os pontos da função
    f(x) = 1/(1 + 25*(x**2))
    de acordo com a formula:
    Xk = -1 + ((2/n)*k)
    """
    x = np.zeros(n, dtype=float)
    for k in range(0,n):
        x[k] = -1 + ((2/n)*k)

    return x

def encontrarPolinomio(n,x):
    """
    Função para retornar o polinomio interpolador 
    conforme os pontos dados
    n = grau
    x = pontos para interpolaçao
    """

    # Definindo Matriz com pontos
    X = np.zeros((n,n), dtype=float)
    # Vetor de coeficientes
    a = np.zeros(n, dtype=float)
    # Vetor de y
    y = np.zeros(n, dtype=float)

    # Preenchendo o vetor y
    for i in range(0,n):
        y[i] = f(x[i])

    # Preenchendo a matrix de X
    for i in range(0,n):
        for j in range(0,n):
            X[i,j] = x[i]**j 

    # Achando os coeficientes por decomposicao LU
    LU = X.copy()
    decompLU(LU)
    a = solveLU(LU,y)

    return a
    
# Definindo o polinomio
def p(z, a, n):
    P = 0

    for i in range(n):
        P += a[i]*(z**i)
    
# Retornando o polinomio
    return P

# Pontos para chebyshev
def pontosChebyshev(n):
    x = np.zeros(n, dtype=float)
    for k in range(n):
        x[k] = math.cos(math.pi*(2*(k+1)-1)/(2*n))
    return x

def normaMaximo(p, f):
    return max(abs(f-p))