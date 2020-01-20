#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import math, sys, termios, tty, os, time 
import random as r

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

def eqsegundogrado(a, b, c):
   sol1, sol2 = mostrarvar(a, b, c)
    
   return sol1, sol2

def mostrarvar(a, b, c):
    """Recopila el valor de las variables de la equacion"""

    print (f"el valor de a es {a}")
    time.sleep(1)
    
    print (f"el valor de b es {b}")
    time.sleep(1)

    print (f"el valor de c es {c}")
    time.sleep(1)

    sol1, sol2 = discriminante(a, b, c)

    return sol1, sol2 

def discriminante(a, b, c):
    """Calcula si la solución es compleja o  """
    dis = b*b-4*a*c
    
    if dis >= 0:
        sol1, sol2 = calcsolnat(a, b, c)

    else:
        print("\nla solucion a la equación introducida es un número complejo\n")
        time.sleep(1)
        sol1 = 0
        sol2 = 0

    return sol1, sol2
        

def calcsolnat(a, b, c):
    """Calcula la solucion a la equacion en base a los datos recopilados previamente"""
    sol1 = (-b + math.sqrt(b*b -4*a*c))/2
    sol2 = (-b - math.sqrt(b*b -4*a*c))/2

    return sol1, sol2
