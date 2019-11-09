import numpy as np
import matplotlib.pyplot as plt
import funcoesInterpolacao as fI

# Letra A
for i in range(2,11):
    
    x = fI.pontos(i) # Pontos
    f = fI.f(x)
    xx = np.linspace(-1,1,100) # Dominio

    # Polinomio gráfico
    pp = np.zeros(len(xx), dtype=float)
    a = fI.encontrarPolinomio(i,x)
    for j in range(len(xx)):
        pp[j] = fI.p(xx[j], a, i)

    #pp = p(xx) # Imagem no gráfico
    xf = fI.f(xx)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Utilizando o conjunto de pontos da letra A")
    plt.plot(xx,xf, 'r',label="Função original")
    plt.plot(xx,pp,label="Função interpoladora")
    plt.legend()
    plt.show()

# Letra B
for i in range(2,11):
    
    x = fI.pontosChebyshev(i) # Pontos
    f = fI.f(x)
    xx = np.linspace(-1,1,100) # Dominio

    # Polinomio gráfico
    pp = np.zeros(len(xx), dtype=float)
    a = fI.encontrarPolinomio(i,x)
    for j in range(len(xx)):
        pp[j] = fI.p(xx[j], a, i)

    #pp = p(xx) # Imagem no gráfico
    xf = fI.f(xx)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Utilizando o conjunto de pontos da letra B")
    plt.plot(xx,xf, 'r',label="Função original")
    plt.plot(xx,pp,label="Função interpoladora")
    plt.legend()
    plt.show()

# Letra C
for i in [2, 5, 10, 15]:
    
    x = fI.pontos(i) # Pontos
    f = fI.f(x)
    xx = np.linspace(-1,1,100) # Dominio

    # Polinomio gráfico
    pp = np.zeros(len(xx), dtype=float)
    a = fI.encontrarPolinomio(i,x)
    for j in range(len(xx)):
        pp[j] = fI.p(xx[j], a, i)

    # Erro
    f1 = fI.f(xx)
    erro = fI.normaMaximo(pp,f1)
    print(erro)

    #pp = p(xx) # Imagem no gráfico
    xf = fI.f(xx)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Utilizando o conjunto de pontos da letra A")
    plt.plot(xx,xf, 'r',label="Função original")
    plt.plot(xx,pp,label="Função interpoladora")
    plt.legend()
    plt.show()