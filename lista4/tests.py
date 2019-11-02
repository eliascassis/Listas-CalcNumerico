import funcoesMatriz as fM 
import numpy as np
import funcoesLeitura as fL
import numpy as np

n_list = [5, 10, 100, 1000]
for n in n_list:
    print("------------------------------------------------------------------------------------")
    print("Para N = ", n)
    print()
    h = fM.construcaoMatrizVetor(n)
    print("Cond(H): ", str.format('{0:.4e}' ,fM.condMatriz(h[0])))
    # Resolvendo o sistema pela Eliminação de Gauss
    h1 = (h[0].copy(), h[1].copy())
    x = fM.gauss(h1[0], h1[1])
    print("Eliminação de Gauss: ", str.format('{0:.4e}' ,fM.calcularResiduo(h[0], h[1], x)))
    # Resolvendo o sistema pela Eliminação de Gauss com Pivotamento
    h2 = (h[0].copy(), h[1].copy()) 
    y = fM.eliminacao_gauss_pivoteamento( h2[0], h2[1])
    print("Eliminação de Gauss c/ pivotamento: ", str.format('{0:.4e}' ,fM.calcularResiduo(h[0], h[1], y)))
    # Resolvendo o sistema pela Decomposição Lu
    h3 = (h[0].copy(), h[1].copy())
    fM.decompLU(h3[0])
    z = fM.solveLU(h3[0], h3[1])
    print("Decomposição LU: ", str.format('{0:.4e}' ,fM.calcularResiduo(h[0], h[1], z)))
    print("------------------------------------------------------------------------------------")
    print()
    quit()

""" #* TESTES ANTERIORES

resultado = fM.construcaoMatrizVetor(5)
print("Matriz")
print(resultado[0])
print("Vetor")
print(resultado[1])

Ai = fM.inversa(A)

print("Inversa")
print(Ai)"""