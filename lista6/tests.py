import numpy as np 
import mmq 

m = 5
x = np.array([0,.25,.5,.75,1], dtype=float)
y = np.array([1,1.280,1.6487,2.1170,2.7183], dtype=float)

A = mmq.sistema_equacoes_normais(x)
