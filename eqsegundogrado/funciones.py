#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import math
import time

import sys
import termios, tty
import tty
import os
 


def getch():
    """Lee un caracter y lo asigna a una variable"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def eqsegundogrado():
   sol1, sol2 = obtenervar()

   return sol1, sol2


def obtenervar():
    """Recopila el valor de las variables de la equacion"""

    a = int(input("introduzca el valor de la variable a:"))
    print (f"el valor de a es {a}")

    b = int(input("introduzca el valor de la variable b:"))
    print (f"el valor de a es {b}")

    c = int(input("introduzca el valor de la variable c:"))
    print (f"el valor de a es {c}")

    print(f"es {a}x*x + {b}x + {c} la equación que desea realizar? Introduzca (R/r) para reiniciar: ")
    res = getch()


    if res == "R" or res == "r":
       print("Reiniciando...")
       time.sleep(2) # espera en segundos
       sol1, sol2 = obtenervar()
    
    else:
       sol1, sol2 = discriminante(a, b, c)


    return sol1, sol2 


def discriminante(a, b, c):
    """Calcula si la solución es compleja o no compleja. """

    dis = b*b-4*a*c
    
    if dis >= 0:
        sol1, sol2 = calcsolnat(a, b, c)

    else:
        print("\nla solucion a la equación introducida es un número complejo\n")
        print (f"desea realizar otra equación? Pulse R o r para reiniciar \n ")
        res = getch()

        if res == "R" or res == "r":
            print("Reiniciando...")
            time.sleep(2) # espera en segundos
            sol1, sol2 = obtenervar()
    
        else:
            exit(0)

    return sol1, sol2
        

def calcsolnat(a, b, c):
    """Calcula la solucion a la equacion en base a los datos recopilados previamente"""

    sol1 = (-b + math.sqrt(b*b -4*a*c))/2
    sol2 = (-b - math.sqrt(b*b -4*a*c))/2

    return sol1, sol2 # Tras este return se activan todos los return hasta llegar a la funcion madre.
