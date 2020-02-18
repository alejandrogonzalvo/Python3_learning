"""

Este programa muestra los datos del alumnado del centro IES El Puig
en orden alfabético.

"""


import csv # Módulo de manipulación de archivos csv.
import os # Manipulación entorno operativo.
import sys # Manipulación entorno operativo.

from colorama import Fore


def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


filename = "ai.csv"

with open(filename) as f:
    reader = csv.reader(f)

    i = 0
    for row in reader:
        if i < 10:
            text1 = Fore.GREEN + row[2]
            text2 = Fore.GREEN + row[3]
            text3 = Fore.RED + row[1]
            text4 = Fore.BLUE + row[0]
            print(text1 + " " + text2 + ", " + text3 + " / " + text4)
            i += 1
            continue

        res = input(Fore.WHITE + "Pulse Enter para continuar, otra tecla para salir:")

        if res == "":
            borrarPantalla()
            i = 0

        else:
            sys.exit()




