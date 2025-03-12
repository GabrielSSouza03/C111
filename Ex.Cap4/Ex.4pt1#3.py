import numpy as np

#criando numpy array 2x2 apenas com zeros 
mtz = np.zeros([2,2])

#adicinonando 1 em uma posição aleatória 
mtz[np.random.randint(0,2),np.random.randint(0,2)] = 1


tentativa=0
max_tentativas=3

while tentativa < max_tentativas:

    print("Digite a posição da matriz que deseja alterar:")
    x = int(input("Digite a linha: "))
    y = int(input("Digite a coluna: "))

    if mtz[x, y] == 1:
        print("Game Over! :( Try Again!")
        break

    tentativa += 1

if tentativa == max_tentativas:
    print("Congratulations! You beat the game! :)")