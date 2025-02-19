kms = int(input("Quantos km irá percorrer? "))


if kms < 200:
    kms = kms * 0.5
    print(f"O valor da viagem será ${kms} ")
else:
    kms = kms * 0.45
    print(f"O valor da viagem será ${kms}")