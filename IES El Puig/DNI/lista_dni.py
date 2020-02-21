# Genera una lista de dni de forma automatizada, y luego la imprime.


import dni


import datetime as d


today = d.date.today()

lista_dni = []
for i in range (3):
    dniaux = dni.creardni(today)
    lista_dni.append(dniaux)

print(lista_dni)