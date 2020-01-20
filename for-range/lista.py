import random as r


lista = []

for x in range(0,10):
    lista.append(r.randrange(0,10000))

print(lista)

r.shuffle(lista)
print(lista)
