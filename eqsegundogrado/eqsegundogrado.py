#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import math
import funciones as f

char = "R"
while (char == "R" or char == "r"):
    char = 0
    sol1, sol2 = f.eqsegundogrado()
    print (f"\nel valor de la solución 1 es {sol1}\n")
    print (f"el valor de la solución 2 es {sol2}\n")
    print (f"desea realizar otra equación? Pulse R o r para reiniciar \n ")
    char = f.getch()
    print("Reiniciando...")
    time.sleep(2) # espera en segundos
