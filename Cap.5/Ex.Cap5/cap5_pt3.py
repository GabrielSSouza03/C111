import numpy as np
import pandas as pd

paises = pd.read_csv('paises.csv')

#1.a 
paises_oceania = paises[paises['Região'].str.contains('OCEANIA')]
print('Países da OCEANIA:')
print(paises_oceania)

#b
print('Número de países da OCEANIA:')
print(len(paises_oceania))

#2 

nome_pais_max_pop = paises.loc[paises['População'].idxmax(), 'País']
regiao_max_pop = paises.loc[paises['População'].idxmax(), 'Região']
print('País com maior população:')
print(nome_pais_max_pop)
print('Região:')
print(regiao_max_pop)

#3

media_alfa = paises.groupby('Região')['Literacy (%)'].mean().reset_index()
print('Média de alfabetização por região:')
print(media_alfa)


#4 
paises_sem_costa = paises[paises['Coastline (coast/area ratio)'] == 0]
paises_sem_costa.to_csv('noCoast.csv', index=False)
print('Países sem costa marítima:')
print(paises_sem_costa[['País', 'Região']])

# #5 
def classifica_mortalidade(mortalidade):
    if mortalidade < 9:
        return 'Balanced'
    else:
        return 'Urgent'
paises['Humanitarian Help'] = paises['Deathrate'].apply(classifica_mortalidade)
print('Dataset com nova coluna "Humanitarian Help":')
print(paises[['País', 'Humanitarian Help']])
