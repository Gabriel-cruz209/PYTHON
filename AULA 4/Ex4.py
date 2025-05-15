n1 = float(input("Digite o numero 1: "))
n2 = float(input("Digite o numero 2: "))

print("Agora digite o resultafo das operações")
res = float(input(f"{n1}+{n2}= "))
resub = float(input(f"{n1}-{n2}= "))
rediv = float(input(f"{n1}/{n2}= "))
remult = float(input(f"{n1}*{n2}= "))

if res == n1 + n2:
    print("Soma: Correto!")
else:
    print("Soma: Errado!")

if resub == n1 - n2:
    print("Subtração: Correto!")
else:
    print("Subtração: Errado!")

if rediv == n1 / n2:
    print("Divisão: Correto!")
else:
    print("Divisão: Errado!")

if remult == n1 * n2:
    print("Multiplicação: Correto!")
else:
    print("Multiplicação: Errado!")

