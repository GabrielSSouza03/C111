
num = int(input("Digite um número entre 1000 e 9999: "))


if 1000 <= num <= 9999:
    
    milhar = num // 1000      
    centena = (num // 100) % 10 
    dezena = (num // 10) % 10  
    unidade = num % 10          

    
    print(f"Milhar: {milhar}")
    print(f"Centena: {centena}")
    print(f"Dezena: {dezena}")
    print(f"Unidade: {unidade}")
else:
    print(" Digite um valor entre 1000 e 9999.")
