n = int(input("Digite o número de clientes: "))

contador = 1
total = 0

while contador <= n:
        temp = float(input(f"Cliente {contador}, digite sua temperatura em ºC: "))
        total += temp

        if temp < 37.2:
            print("Temperatura normal.")
        elif 37.2 <= temp < 38:
            print("Estado febril.")
        elif 38 <= temp <= 39:
            print("Com febre.")
        elif temp > 39:
            print("Com febre alta.")
        else:
            print("Temperatura inválida.")

        contador += 1

media = total / n
print(f"\nQuantidade de pessoas analisadas: {n}")
print(f"Média das temperaturas: {media:.2f} ºC")

        
      