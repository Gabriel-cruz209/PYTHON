temperatura = float(input("Digite sua temperatura"))
if temperatura <= 37.2:
    print("Sua temperatura está normal")
elif temperatura <= 38:
    print("Você está em estado febril")
elif temperatura <= 39:
    print("Você está com febre")
else:
    print("Você está com febre alta")