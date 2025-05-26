lista = [4,5,3,5]
print(lista)#[4, 5, 3, 5]

lista.append(2)
print(lista)#[4, 5, 3, 5, 2]

lista.insert(2,-3)
print(lista)#[4, 5, -3, 3, 5, 2]

lista.remove(4)
print(lista)#[5, -3, 3, 5, 2]

lista.sort()
print(lista)

lista.reverse()
print(lista)

qnt = lista.count(5)
print(qnt)

exc = lista.pop()
print(lista)
print(exc)
del lista[2]
print(lista)
del lista[2:5]
print(lista)
lista.clear()
print(lista)