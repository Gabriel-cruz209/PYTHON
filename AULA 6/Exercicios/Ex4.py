n = int(input("Quantas pessoas serão analisadas? "))

contador = 0
somaMulheres = 0
somaHomens = 0
quantMulheres = 0
quantHomens = 0
soma = 0

while contador < n:
    idade = int(input(f"\nDigite a idade da pessoa {contador + 1}: "))
    sexo = input("Digite o sexo (M para masculino, F para feminino): ").strip().upper()

    if sexo == "F":
        somaMulheres += idade
        quantMulheres += 1
    elif sexo == "M":
        somaHomens += idade
        quantHomens += 1
    else:
        print("Sexo inválido. Use apenas 'M' ou 'F'.")
        

    soma += idade
    contador += 1


mediaMulheres = somaMulheres / quantMulheres if quantMulheres > 0 else 0
mediaHomens = somaHomens / quantHomens if quantHomens > 0 else 0
mediaGrupo = soma / n

print("\nResultados:")
print(f"Idade média das mulheres: {mediaMulheres:.2f}")
print(f"Idade média dos homens: {mediaHomens:.2f}")
print(f"Idade média do grupo: {mediaGrupo:.2f}")