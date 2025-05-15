A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

A += B
B -= A
A += B
B *= -1

print(f"OS valores de trocas são :  {A}")
print(f"OS valores de trocas são :  {B}")