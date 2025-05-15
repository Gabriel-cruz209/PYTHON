def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

n = int(input("Digite um numero"))
print(f'O fatorial é: {fatorial(n)}')