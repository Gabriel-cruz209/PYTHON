#Ler do teclado a idade e o sexo de 10 pessoas,Calcule e imprima
# Inicializando variáveis de controle
tidadem = 0
tm = 0
tidadeh = 0
th = 0
tidadeg = 0

for i in range(1, 11):
    print(f"Pessoa {i}:")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper() 

    tidadeg += idade

    if sexo == 'F':
        tidadem += idade
        tm += 1
    elif sexo == 'M':
        tidadeh += idade
        th += 1

mm = tidadem / tm if tm > 0 else 0
mh = tidadeh / th if th > 0 else 0
mg = tidadeg / 10


print(f"\nIdade média das mulheres: {mm:.2f}")
print(f"Idade média dos homens: {mh:.2f}")
print(f"Idade média do grupo: {mg:.2f}")

    