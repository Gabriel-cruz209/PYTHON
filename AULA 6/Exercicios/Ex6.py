while True:
    mensagem = input("Digite o nome de usuário: ")

    if mensagem == "":
        print("O usuário não digitou.")
        break

    invertido = mensagem[::-1]
    print(f"Nome invertido: {invertido}")