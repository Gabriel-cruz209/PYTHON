bancos = ["Banco do Brasil","Caixa","Santander"]
print(bancos)
#Resultado:["Banco do Brasil", "Caixa", "Santander"]
bancos[1] = "Itaú"
print(bancos)
#Resultado:["Banco do Brasil", "Itaú", "Santander"]
bancos[-1] = "C6"#O -1 significa q substitui o ultimo
print(bancos)
##Resultado:["Banco do Brasil", "Itaú", "C6"]
bancos = bancos + ["Bradesco", "Nubank"]
print(bancos)
##Resultado:["Banco do Brasil", "Itaú", "C6","Bradesco", "Nubank"]
bancos+= ["Safra"]
print(bancos)
##Resultado:["Banco do Brasil", "Itaú", "C6","Bradesco", "Nubank", "Safra"]
