compra = [10.2, 3.35, 16.3,["tomate","sabotene","arroz"]]
print(compra)#[10.2, 3.35, 16.3, ['tomate', 'sabotene', 'arroz']]

produtos = compra[3]
print(produtos)#['tomate', 'sabotene', 'arroz']

total = compra[0]+compra[1]+compra[2]
print(total)#29.85

letra = ["a", "b", "c"]
num = [2,4,6]
tudo = [letra,num]
print(tudo)#[['a', 'b', 'c'], [2, 4, 6]]
print(f"Letras: {tudo[0]}")#Letras: ['a', 'b', 'c']
print(f"Numeros: {tudo[1]}")#Numeros: [2, 4, 6]

#len = tamanho da nossa lista
# index = obter indice de determinado elemento

letra =["a","b","c"]
print(f"tamanho da lista: {len(letra)}")
print(f"endereço da letra b: {letra.index('b')}")