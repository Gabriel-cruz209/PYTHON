n = int(input("Digite um número: "))

fatorial = 1
conta = n

while conta > 1:
    fatorial *= conta
    conta -= 1

print(f"Fatorial de {n}: {fatorial}")