while True:
    n1 = int(input("Digite o número que você quer treinar a tabuada: "))
    acertos = 0
    erros = 0

    contador = 1
    while contador <= 10:
        resposta = int(input(f"{n1} x {contador} = "))
        resultado = n1 * contador

        if resposta == resultado:
            print("Correto")
            acertos += 1
        else:
            print(f"Que pena, você errou, o valor correto é: {resultado}")
            erros += 1

        contador += 1

    print(f"\nTotal de acertos: {acertos}")
    print(f"Total de erros: {erros}")
