import numpy as np 
import mmq 
import matplotlib.pyplot as plt
import leitura as l

# Inicializando a lista de Ns
listN = [1,2,3,5,7]

x, y = l.leitura("ex1_dados.txt")

for n in listN:

    # Aplicando o método
    A = mmq.sistema_equacoes_normais(x, n+1) # Sistema de equações normais
    M = mmq.m(A) # M = AA^T
    F = mmq.f(A, y) # F = A^Ty

    # Resolvendo pelo método de Cholesky
    A = mmq.cholesky(M) 
    c = mmq.solveCholesky(A, F)
    print(c)
    # Definindo a função aproximada
    z = np.arange(0, 5, 0.0001)
    result = np.zeros(len(z), dtype=float)
    for i in range(len(z)):
        for j in range(n+1):
            result[i] += c[j]*(z[i] ** j)

    print("\nN = %d" % n)
    print("E_q = %f" % mmq.quadradosMedPred(result, y, n))
    print("Media = %f" % mmq.media(y, n))
    print("E_qm = %f" % mmq.quadradosDifMedia(y, n))
    print("R^2 = %f" % mmq.coefDeterminacao(result, y, n))

    # Plotando o gráfico
    plt.title("Aproximação pelo MMQ utilizando polinômio de grau {}".format(n))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.scatter(x,y,label="Pontos experimentais", color='green')
    plt.plot(z, result, label="Aproximação pelo MMQ")
    plt.legend()
    plt.show()