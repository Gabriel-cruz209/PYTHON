altura = float(input("Digite a altura do reservatório em centimetros: "))
comprimento = float(input("Digite o comprimento do reservatório em centimetros: "))
largura = float(input("Digite a largura  do reservatório em centimetros: "))
consumoDiario = float(input("Digite o consumo médio diário (litros/dia): "))

cm3 = altura * comprimento* largura
litros = cm3 / 1000
autonomia = litros / consumoDiario

if autonomia < 2:
    print("Classificação: Consumo Elevado")
elif autonomia <= 7:
    print("Classificação: Consumo Moderado")
else:
    print("Classificação: Consumo Reduzido")


print(f"A capacidade total da caixa d'agua em litros é: {litros}")
print(f"A autonomia do reservatório em dias é: {autonomia}")
