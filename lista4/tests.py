import funcoesMatriz as fM 
import numpy as np
import funcoesLeitura as fL
import numpy as np

n_list = [1000]
for n in n_list:
    print("------------------------------------------------------------------------------------")
    print("Para N = ", n)
    print()
    h = fM.construcaoMatrizVetor(n)
    print("Cond(H): ", fM.condMatriz(h[0]))
    # Resolvendo o sistema pela Eliminação de Gauss
    x = fM.gauss(h[0], h[1])
    print("Eliminação de Gauss: ", str.format('{0:.4e}' ,fM.calcularResiduo(h[0], h[1], x)))
    # Resolvendo o sistema pela Eliminação de Gauss com Pivotamento 
    x = fM.eliminacao_gauss_pivoteamento( h[0], h[1])
    print("Eliminação de Gauss c/ pivotamento: ", str.format('{0:.4e}' ,fM.calcularResiduo(h[0], h[1], x)))
    # Resolbendo o sistema pela Decomposição Lu
    x = fM.solveLU(h[0], h[1])
    print("Decomposição LU: ", str.format('{0:.4e}' ,fM.calcularResiduo(h[0], h[1], x)))
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