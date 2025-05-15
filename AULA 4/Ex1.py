P1 = int(input("Digite a quatidade de gols do time 1: "))
P2 = int(input("Digite a quatidade de gols do time 2: "))
if P1 > P2:
    print("O time 1 é o vencedor")
elif P1 == P2:
    print("O jogo deu empate")
else:
    print("O time 2 é o vencedor")