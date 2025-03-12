import numpy as np

#criando array unidimensional de n pares de 0 a 51
arr1 = np.arange(0,52,2)

#criando array unidimensional de n pares de 100 até 50
arr2 = np.arange(100,49, -2)

#concatenando os arrays e mostrando o resultado 
print(arr1)
print(arr2)
print(np.concatenate((arr1,arr2)))