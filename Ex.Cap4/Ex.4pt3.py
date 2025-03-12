import numpy as np
# carregando  o dataset space.csv
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
#a
# Contar quantas missões foram bem-sucedidas
success_count = np.sum(dataset[:, -1] == 'Success')


total_missions = len(dataset)

# Calcular a porcentagem de missões que deram certo
success_percentage = (success_count / total_missions) * 100

#b
#media das gastos nas missoes 

custs_missons= np.mean(dataset[:,-2].astype(float))


#c 
# calcular quantidade de missoes realizadas pelos EUA
usa_missions = np.sum(dataset[:, 0] == 'USA')

#d

# Encontrar missão mais cara realizada pela SpaceX
spacex_missions = dataset[dataset[:, 1] == 'SpaceX']
most_expensive = np.max(spacex_missions[:, -2].astype(float))

#e

# Mostrando o nome das empresas que já realizaram missões espaciais,juntamente com suas respectivas quantidades de missões
empresas = np.unique(dataset[:, 1], return_counts=True)
for empresa, count in zip(empresas[0], empresas[1]):
    print(f'Empresa: {empresa}, Quantidade de missões: {count}')
