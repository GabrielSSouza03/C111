nome = input("Qual seu nome completo? ")

print(f"Seu nome com apenas letras maiúsculas: {nome.upper()}")


print(f"Seu nome com apenas letras minúsculas: {nome.lower()}")


quantidadeLetras = len(nome.replace(" ", ""))
print(f"Número total de letras: {quantidadeLetras}")

nomes = nome.split()
if len(nomes) > 1:
    nomes[-1] = "do Inatel"
else:
    nomes.append("do Inatel")

novo_nome = " ".join(nomes)
print(f"Nome modificado: {novo_nome}")
