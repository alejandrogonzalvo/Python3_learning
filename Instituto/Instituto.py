import csv

sitios = []

with open('sitios.csv', newline='') as File:
    reader = csv.reader(File)

    for row in reader:
        sitios.append(row)


departamentos = []

with open('departamentos.csv', newline='') as File:
    reader = csv.reader(File)

    for row in reader:
        departamentos.append(row)


instituto = {
    'Nombre': 'IES El Puig',
    'Sitios': sitios,
    'departamentos': departamentos
}

print (instituto)
