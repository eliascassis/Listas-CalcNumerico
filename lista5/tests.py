import numpy as np
import matplotlib.pyplot as plt
import funcoesInterpolacao as fI

for i in range(3,11):
    
    x = fI.pontos(i) # Pontos
    f = fI.f(x)
    xx = np.linspace(-1,1,100) # Dominio

    # Polinomio gráfico
    pp = np.zeros(len(xx), dtype=float)
    a = fI.encontrarPolinomio(i,x)
    for j in range(len(xx)):
        pp[j] = fI.p(xx[j], a, i)

    #pp = p(xx) # Imagem no gráfico
    plt.plot(x,f)
    plt.plot(xx,pp)
    plt.show()
    #quit()