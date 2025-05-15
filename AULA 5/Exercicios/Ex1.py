
texto = "Numeros pares: "
soma = 0
for numero in range (0, 101, 2):
    texto = texto + str(numero)
    if numero > 101:
        texto = texto + "\nPassou de 100"
        break
    if numero != 101-1:
        texto = texto + ","
print(f"{texto}")
