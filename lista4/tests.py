import funcoesMatriz as fM 
import numpy as np
import funcoesLeitura as fL
import numpy as np

A = np.array(([5,-2],[-2,4]), dtype=float)
print(fM.condMatriz(A))

""" #* TESTES ANTERIORES

resultado = fM.construcaoMatrizVetor(5)
print("Matriz")
print(resultado[0])
print("Vetor")
print(resultado[1])

Ai = fM.inversa(A)

print("Inversa")
print(Ai)"""