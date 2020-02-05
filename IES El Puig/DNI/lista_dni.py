# Genera una lista de dni de forma automatizada, y luego la imprime.


from dni import creardni


lista_dni = []
for i in range (3):
    dniaux = creardni()
    lista_dni.append(dniaux)

print(lista_dni)