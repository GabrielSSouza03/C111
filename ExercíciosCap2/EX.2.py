
num = int(input("Esolha um número: "))


inicio = int(input("Digite o valor inicial do intervalo: "))
fim = int(input("Digite o valor final do intervalo: "))


if inicio > fim:
    inicio, fim = fim, inicio  


print(f"\nTabuada do {num} de {inicio} até {fim}:\n")
for i in range(inicio, fim + 1):
    print(f"{num} x {i} = {num * i}")
