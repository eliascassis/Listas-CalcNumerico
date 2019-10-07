import funcoesMatriz as fM 
import funcoesLeitura as fL

resultado = fM.construcaoMatrizVetor(5)
print("Matriz")
print(resultado[0])
print("Vetor")
print(resultado[1])

Ai = fM.inversa(resultado[0])

print("Inversa")
print(Ai)
