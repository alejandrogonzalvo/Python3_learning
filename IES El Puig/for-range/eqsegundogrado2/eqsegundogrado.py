#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# Este programa genera numeros de forma pseudo aleatoria y los utiliza como valores para resolver una equación de segundo grado.

import math
import funciones as f
import random as r
import time as t




coef = []
soluciones = []

for x in range(3):
    coef.append(r.randrange(100))
    coef.append(r.randrange(100))
    coef.append(r.randrange(100))

while True:
    
        
    try:
        a = coef.pop(-1)
        b = coef.pop(-1)
        c = coef.pop(-1)
    
    except IndexError:
        print("\nYa no quedan mas datos en la lista")
        print("Resultados obtenidos:\n")
        print(soluciones)
        break

    sol1, sol2 = f.eqsegundogrado(a,b,c)
    soluciones.append({(f'{a}x*x', f'{b} x', f'{c}') : (f'{sol1} , {sol2}')}) # almacena los coeficientes y las soluciones en un diccionario. 
    print (f"\nel valor de la solución 1 es {sol1}\n")
    print (f"el valor de la solución 2 es {sol2}\n")
    print("Reiniciando...")
    t.sleep(2) # espera en segundos

