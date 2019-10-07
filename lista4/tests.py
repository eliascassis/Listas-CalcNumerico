import funcoesMatriz as fM 
import numpy as np

m = np.zeros((2,2), dtype=float)
for i in range(2):
    for j in range(2):
        m[i,j] = float(input())
mi = fM.inversa()