while True:
    sexo = input("Digite o sexo (M para homem, F para mulher): ")
    
    if sexo == "M":
        print("Você é homem.")
        break
    elif sexo == "F":
        print("Você é mulher.")
        break
    else:
        print("Entrada inválida! Por favor, digite 'M' para homem ou 'F' para mulher.")
d