import numpy as np
import pandas as pd

# 1

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

#2 
print(seriesAno1.sum())
print(seriesAno2.sum())

#3 
changes = seriesAno2 - seriesAno1

#4 Baseado nos resultados da Questão 3, mostre apenas os dados das
#linguagens que tiveram crescimento;
print(changes[changes > 0])

# 5 
print((seriesAno2 + changes).nlargest(1))


np.random.seed(10)
df = pd.DataFrame(
index=['A','B', 'C', 'D', 'E'],
columns=['W', 'X', 'Y', 'Z'],
data=np.random.randint(1, 50, [5, 4]))

#6
print(df[df['X'] < 30]['X'].mean())

#7 
print(df.loc['D'].mean())

#8 
print(df.loc[['A', 'C', 'E'], ['X', 'Y']])