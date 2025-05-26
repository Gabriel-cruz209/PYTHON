notas = 0
quant = 0
while True:
   nota = float(input("Informe  nota: (-1 para finalizar):"))
   if (nota ==-1):
    break
notas = notas + nota
quant = quant + 1
if quant > 0:
   media = notas/quant
   print(f"Quantidade notas informados: {quant}")
   print(f"Media: {media:.2f}")
else:
  print("Nenhuma nota informação")
