#EX1 

classificacao = ["Real Madrid", "Manchester City", "Barcelona", "Bayern de Munique", "Arsenal"]


print("Top 3 times:", classificacao[:3])

print("Últimos 2 times:", classificacao[-2:])


print("Times em ordem alfabética:", sorted(classificacao))

posicao_barcelona = classificacao.index("Barcelona") + 1
print(f"O Barcelona está na {posicao_barcelona}ª posição da tabela.")

#EX2

loja1 = {"iPhone 13", "Samsung Galaxy S22", "Xiaomi Mi 11", "OnePlus 9"}
loja2 = {"iPhone 13", "Samsung Galaxy S21", "Xiaomi Mi 11", "Google Pixel 6"}

modelos_totais = loja1.union(loja2)
print("Modelos disponíveis no total:", modelos_totais)

modelos_comuns = loja1.intersection(loja2)
print("Modelos disponíveis em ambas as lojas:", modelos_comuns)

#EX3

nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

situacao = "AP" if media >= 50 else "RP"

aluno = {
    "Nome": nome,
    "Média": media,
    "Situação": situacao
}

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")


#EX4

pessoas = []
for i in range(3):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    peso = float(input(f"Digite o peso de {nome} (kg): "))
    pessoas.append((nome, peso))

mais_pesada = max(pessoas, key=lambda x: x[1])
mais_leve = min(pessoas, key=lambda x: x[1])

print("\nPessoa mais pesada:", mais_pesada[0], "com", mais_pesada[1], "kg")
print("Pessoa mais leve:", mais_leve[0], "com", mais_leve[1], "kg")


#EX5

pessoas = []
n = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(n):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    sexo = input(f"Digite o sexo de {nome} (M/F): ").strip().upper()
    pessoas.append({"Nome": nome, "Idade": idade, "Sexo": sexo})

media_idade = sum(p["Idade"] for p in pessoas) / n

mulheres_menos_20 = sum(1 for p in pessoas if p["Sexo"] == "F" and p["Idade"] < 20)

print("\nMédia de idade do grupo:", media_idade)
print("Número de mulheres com menos de 20 anos:", mulheres_menos_20)