import math 


num = float(input("Entre com um número decimal: "))


raiz_quadrada = math.sqrt(num)
teto = math.ceil(num)
chao = math.floor(num)
parte_inteira = int(num)

print(f"\nNúmero: {num}")
print(f"Raiz quadrada: {raiz_quadrada:.2f}")
print(f"Função teto: {teto}")
print(f"Função chão : {chao}")
print(f"Parte inteira: {parte_inteira}")
