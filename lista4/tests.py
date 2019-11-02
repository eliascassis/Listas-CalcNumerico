import funcoesMatriz as fM 
import numpy as np
import funcoesLeitura as fL
import numpy as np

A = np.array(([4,0.24,-0.08],[0.09,3,-0.15],[0.04,-0.08,4]), dtype=float)
b = np.array(([8,9,20]), dtype=float)
x0 = np.zeros(3, dtype=float)
print(fM.gaussSeidel(A, b, x0))


# print(fM.condMatriz(A, Ai))

""" #* TESTES ANTERIORES

resultado = fM.construcaoMatrizVetor(5)
print("Matriz")
print(resultado[0])
print("Vetor")
print(resultado[1])

Ai = fM.inversa(A)

print("Inversa")
print(Ai)"""