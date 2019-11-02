import funcoesMatriz as fM 
import numpy as np
import funcoesLeitura as fL
import numpy as np

n_list = [5]
for n in n_list:
    print(n)
    h = fM.construcaoMatrizVetor(n)
    print("Cond(H): ", fM.condMatriz(h[0]))
    # Resolvendo o sistema pela Eliminação de Gauss
    x = fM.gauss(h[0], h[1])
    print(fM.calcularResiduo(h[0], h[1], x))
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