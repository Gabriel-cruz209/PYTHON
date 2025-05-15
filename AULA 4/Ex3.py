id = int(input("Digite a idade do nadador: "))
if id <= 7:
    print("A categoria é Infantil A")
elif id <= 11:
    print("A categoria é Infantil B")
elif id <= 13:
    print("A categoria é Juvenil A")
elif id <= 17:
    print("A categoria é Juvenil B")
else:
    print("A idade é maior que 18 anos")