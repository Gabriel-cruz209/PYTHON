#Calculadora de juros compostos
print("Bem vindo a calculadora de juros compostos\n")
valor = float(input("Digite o valor inicial"))
parcela = int(input("Digite quantos a quantidade de meses"))
taxa = float(input("Digite a taxa do juros"))

taxad = taxa / 100

jcompostos = valor * ((1 + taxad)** parcela)

print(f"O valor de {valor:.2f} a uma taxa de {taxa:.2f}% a um periodo de {parcela} meses é: {jcompostos:.2f}")