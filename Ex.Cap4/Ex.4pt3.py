import numpy as np
# carregando  o dataset space.csv
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')


# Verifique o número de colunas e as primeiras linhas do dataset para localizar a coluna de sucesso
print(dataset[:5])  # Mostra as primeiras 5 linhas para verificar o formato

# Suponhamos que a última coluna tenha a informação sobre o sucesso da missão.
# Caso a coluna de sucesso seja diferente, altere o índice para a coluna correta.

# Contar quantas missões foram bem-sucedidas
success_count = np.sum(dataset[:, -1] == 'Success')

# Calcular o total de missões
total_missions = len(dataset)

# Calcular a porcentagem de missões que deram certo
success_percentage = (success_count / total_missions) * 100