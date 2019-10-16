import funcoesMatriz as fM 
import numpy as np
import funcoesLeitura as fL

m = np.zeros((2,2), dtype=float)
for i in range(2):
    for j in range(2):
        m[i,j] = float(input())
mi = fM.inversa(m)
print(fM.condMatriz(m, mi))

"""resultado = fM.construcaoMatrizVetor(5)
print("Matriz")
print(resultado[0])
print("Vetor")
print(resultado[1])

Ai = fM.inversa(resultado[0])

print("Inversa")
print(Ai)"""