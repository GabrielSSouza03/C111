#1

#importando numpy 
import numpy as np 

#criando numpy array unidimensional de tamanho 8 apneas com zeros
arr1 = np.zeros(8)

#criando numpy array unidimensional de tamanho 8  com numeros aleatórios entre 0 e 9
arr2 = np.random.randint( 0,10,8)

arr_sum = arr1 + arr2

#Se a soma de todos os elementos do Array resultante for >= 40, remodele este NumPy Array para se tornar uma matriz com mais linhas do que colunas. Senão, remodele para que se torne uma matriz com mais colunas do que linhas.  

if arr_sum.sum() >= 40:
    arr_sum = arr_sum.reshape(4,2)
else: 
    arr_sum = arr_sum.reshape(2,4)

print(arr_sum)

