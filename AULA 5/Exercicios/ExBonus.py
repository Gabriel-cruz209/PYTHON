n1 = int(input("Digite o número que você quer treinar a tabuada: "))
acertos = 0
erros = 0
for i in range(1, 11):
    resposta = int(input(f"{n1} x {i} = "))
    resultado = n1 * i
    if resposta == resultado:
        print("Correto")
        acertos += 1
    else:
        print(f"Que pena, você errou, o valor correto é: {resultado}")
        erros += 1
print(f"\nTotal de acertos: {acertos}")
print(f"Total de erros: {erros}")