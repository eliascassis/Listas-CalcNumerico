import numpy as np 
import mmq 
import matplotlib.pyplot as plt

# Inicializando a lista de Ns
listN = [1,2,3,5,7]

for n in listN:
    # Definindo pontos necessários
    m = n
    #x = np.array([0,.25,.5,.75,1], dtype=float)
    #y = np.array([1,1.280,1.6487,2.1170,2.7183], dtype=float)

    # Aplicando o método
    A = mmq.sistema_equacoes_normais(x) # Sistema de equações normais
    M = mmq.m(A) # M = AA^T
    F = mmq.f(A, y) # F = A^Ty

    # Resolvendo pelo método de Cholesky
    A = mmq.cholesky(M) 
    c = mmq.solveCholesky(M, F)
    # Definindo a função aproximada
    z = np.arange(0, 1, 0.0001)
    result = np.zeros(len(z), dtype=float)
    for i in range(len(z)):
        result[i] = c[0] + c[1]*z[i] + c[2]*(z[i] ** 2)

    # Plotando o gráfico
    plt.title("Aproximação de função pelo método dos mínimos quadrados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.scatter(x,y,label="Pontos experimentais", color='green')
    plt.plot(z, result, label="Aproximação pelo MMQ")
    plt.legend()
    plt.show()