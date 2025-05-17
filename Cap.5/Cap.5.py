import numpy as np 
import pandas as pd

# SERIES 
labels = [ 'a','b','c']
dados = [10,20,30]

# Criando uma Series com duas listas
s1 = pd.Series(index=labels, data=dados)
# Criando uma Series com um dicionário
s2 = pd.Series({'a':10, 'c':50, 'd':80})
print(s1)
print(type(s1))

# chamando um valor da Series
print(s1['b'])

# Operações entre as Series 
#print(s1 +s2)

#print(s1.add(s2, fill_value=0))

# Acessar apenas o que precisamos 
# print(s1[['a','c']])

# Condicionais do Pandas (identico ao NumPy)
print(s1>s1.mean())
print(s1[s1 > s1.mean()])


# DATAFRAME

# Plantando uma semente aleatória
np.random.seed(10)

# Criando um Dataframe

df = pd.DataFrame(index=['A','B','C','D','E'],
                  columns=['W','X','Y','Z'],
                  data= np.random.randint(1, 50, [5,4]))

print(df)

#Slicing com múltiplas colunas
print(df[['W','Z']])

# Acessando um elemento do DataFrame
#coluna seguido de linha 
print(df['X']['B'])

# Fazendo Slicing com loc() ou iloc()
# Slicing com loc()
print( df.loc[['A','B'],['W','X','Y','Z']])
# Slicing com iloc()
print(df.iloc[0:2,:])


