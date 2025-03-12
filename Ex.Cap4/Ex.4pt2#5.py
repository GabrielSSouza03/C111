import numpy as np 

#criando uma matriz  4x4 formada por números aleatórios inteiros entre 1 e 50 (use seed = 10 antes)
np.random.seed(10)
mtz = np.random.randint(1,51,(4,4))
print(mtz)

# mostrando o resultado da média de cada linha e cada coluna da matriz gerada 
mediaLinhas = mtz.mean(axis=1)
mediaColunas = mtz.mean(axis=0)
print("Média das linhas: ", mediaLinhas)
print("Média das colunas: ", mediaColunas)

#b
print(mediaLinhas.max())
print(mediaColunas.max())

# Imprimindo a quantidade de aparições de cada um dos números gerados na matriz
unique, counts = np.unique(mtz, return_counts=True)
print(dict(zip(unique, counts)))


#imprimindo apenas os números que aparecem 2 vezes
unique, counts = np.unique(mtz, return_counts=True)
print(unique[counts == 2])

