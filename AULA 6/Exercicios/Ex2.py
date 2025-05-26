seq = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
while True:
    print(seq[i])
    break

maior = max(seq)
menor = min(seq)
total = 0

while i < 10:
    total += seq[i]
    i += 1
media = total / 10

print(f"O maior é: {maior}  E o menor é: {menor} A média é: {media}")