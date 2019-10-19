import funcoesMatriz as fM 
import funcoesLeitura as fL
import numpy as np

A = np.array(([1,3,3],[1,4,3],[1,3,4]))

Ai = fM.inversa(A)

print("Inversa")
print(Ai)
