import numpy as np 

dataset = np.loadtxt('paises.csv', delimiter=';', skiprows=1,dtype=str)

#1
#Faça um slicing no dataset para mostrar apenas o País (Country), Região (Region), População (Population) e Area (Area (sq. mi.)) dos países contidos nele;
print(dataset[:, [0, 1, 2, 3]])


#2
#Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo este dataset;
print(np.unique(dataset[:,1]))

#3
#Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo este dataset;
print(np.mean(dataset[:,10].astype(float)))

#4
#Conte quantos países são da América do Norte (NORTHERN AMERICA) segundo este dataset;
print(np.sum(np.char.strip(dataset[:, 1]) == 'NORTHERN AMERICA'))

#5
#Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) possui a maior renda per capita (GDP ($ per capita));

americaDoSulCaribe = dataset[np.char.strip(dataset[:, 1]) == 'LATIN AMER. & CARIB']

gdp_per_capita = np.where(americaDoSulCaribe[:, 8] == '', '0', americaDoSulCaribe[:, 8]).astype(float)

paisComMaiorPerCapita = americaDoSulCaribe[gdp_per_capita.argmax()]
print(paisComMaiorPerCapita[0])