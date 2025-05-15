seq = [1,2,3,4,5,6,7,8,9,10]
for n2 in seq:
        print(n2)
        break
maior = max(seq)
menor = min(seq)
total = 0
for numero in range(1, 10):
    total += numero
print(total) 
média = total / 10
print(f"Números inteiros: {seq}  O maior é: {maior}  E o menor é: {menor} a média é: {média}")