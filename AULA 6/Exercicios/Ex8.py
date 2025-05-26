while True:
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite sua senha: ")

    if usuario == senha:
        print("Erro: usuário e senha não podem ser iguais. Digite novamente.\n")
    else:
        print("Usuário e senha corretos.")
        break