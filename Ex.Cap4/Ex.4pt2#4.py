import numpy as np 
#criando uma matriz de tamanho qualquer e com numeros aleatorios 
mtz = np.random.randint(0,10,(3,3))

#multiplicando nº de linhas pelo nº colunas 
mtz_size = mtz.shape[0] * mtz.shape[1]

if mtz_size % 2 == 0:
    print("A matriz pode ser um vetor unidimensional com número par de elementos")

else:
    print("A matriz pode ser um vetor unidimensional com número ímpar de elementos")