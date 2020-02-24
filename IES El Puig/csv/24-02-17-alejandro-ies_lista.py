"""

Este programa muestra los datos del alumnado del centro IES El Puig
en orden alfabético.

"""


import csv # Módulo de manipulación de archivos csv.
import os # Manipulación entorno operativo.
import sys # Manipulación entorno operativo.

from colorama import Fore


def borrarPantalla():
    nw = {"ce", "nt", "dos"} 
    if os.name == "posix":
        os.system ("clear")
    elif os.name in nw:
        os.system ("cls")


filename = "/home/alejandrogonzalvo4eso/Escritorio/python3_learning/IES El Puig/csv/ai.csv"

with open(filename) as f:
    reader = csv.reader(f)

    i = 0

    for row in reader:
        fields = []
        if i < 10:
            for r in range(4):
                field = ""
                for ch in row[r]:
                    field += ch
                
                while len(field) < 20:
                    field += " "

                fields.append(field)


            text1 = Fore.GREEN + fields[2]
            text2 = Fore.GREEN + fields[3]
            text3 = Fore.RED + fields[1]
            text4 = Fore.BLUE + fields[0]
            print("\n" + text1 + " " + text2 + ", " + text3 + " / " + text4)
            i += 1
            continue

        res = input(Fore.WHITE + "Pulse Enter para continuar, otra tecla para salir:")

        if res == "":
            borrarPantalla()
            i = 0

        else:
            sys.exit()




