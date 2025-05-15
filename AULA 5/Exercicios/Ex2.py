valor = [1,2,3,4,5,6,7,8,9,10]
for n2 in valor:
        print(n2)
        break
maior = max(valor)
menor = min(valor)
total = 0
for numero in range(1, 10):
    total += numero
print(total) 
média = total / 10
print(f"Números inteiros: {valor} ")
print(f"O maior é: {maior}")
print(f"O menor é: {menor}")
print(f"A média é: {média}")