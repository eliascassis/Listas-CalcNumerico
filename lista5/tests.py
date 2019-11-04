import numpy as np
import matplotlib.pyplot as plt
import funcoesInterpolacao as fI

for i in range(2,11):
    
    x = fI.pontos(i) # Pontos
    f = fI.f(x)

    xx = np.linspace(-1,1,100) # Dominio

    p = fI.encontrarPolinomio(i,x) # Polinomio gráfico

    pp = p(xx) # Imagem no gráfico

    plt.plot(x,f)
    plt.plot(xx,pp)