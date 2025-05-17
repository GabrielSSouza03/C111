import numpy as np 
import pandas as pd

#import de dados no PANDAS

df = pd.read_csv('paises.csv', delimiter= ';')
print(df.columns)
print(df.head(3))
print(df.tail(3))

#calular a % da população de cada pais no plaeta 
total_pupulation = np.sum(df['Population'])
print(total_pupulation)

#calculando a porcentagem de cada pais
seriesPercPopulation = (df['Population']/total_pupulation)*100
print (seriesPercPopulation)

# criando uma nova coluna no dataset
df['%Population'] = seriesPercPopulation

#gerando um novo arquivo com a nova coluna
df.to_csv('paises2.csv',sep=';')

#pegando os 6 paises mais populosos do planeta 
print(df.nlargest(6,'%Population'))

#agrupando os dados por região 
group_region = df.grouby('Region')
print(group_region.count()['Country'])
print(group_region.sum()['Population'])

#criando um metodo no python 
def tenpercent(x):
    return x*0.9

# pegando a taxa de mortalidade
taxa_mortalidade = df['Deathrate']

#aplicando a funçao customizada em uma series
taxa_mortalidade2 = df['Deathrate'].apply(tenpercent)

#juntando duas series
print(pd.concat([taxa_mortalidade, taxa_mortalidade2], axis=1))