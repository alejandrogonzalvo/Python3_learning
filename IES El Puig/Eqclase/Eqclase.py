# !/usr/bin/python3.5


import math
import time


class Eqsegundogrado:
    """Estructura de datos con formato de equación de segundo grado y funciones de interacción con sus respectivos algoritmos."""


    def __init__(self, a = 0, b = 0, c = 0):

        self.a = a
        print (f"el valor de a es {self.a}")

        self.b = b
        print (f"el valor de b es {self.b}")

        self.c = c
        print (f"el valor de c es {self.c}")

        self.dis = self.b*self.b-4*self.a*self.c

        print(f"\n{self.a}x*x + {self.b}x + {self.c} es la nueva equación")


    def __str__(self):
        return '{self.a}x*x + {self.b}x + {self.c} es la equación actual'.format(self=self)

    def redef(self):
        """Recopila el valor de las variables de la equacion"""

        self.a = int(input("introduzca el nuevo valor de la variable a:"))
        print (f"el valor de a es {self.a}")

        self.b = int(input("introduzca el nuevo valor de la variable b:"))
        print (f"el valor de a es {self.b}")

        self.c = int(input("introduzca el nuevo valor de la variable c:"))
        print (f"el valor de a es {self.c}")

        print(f"{self.a}x*x + {self.b}x + {self.c} es la nueva equación")

    def tiposol(self):

        if self.dis > 0:
            print("La equacion tiene dos soluciones reales.")

        elif self.dis = 0:
            print("La equacion solo tiene una solucion real (0).")

        else:
            print("La equacion tiene 2 soluciones imaginarias.")


    def resolver(self):
    
        if self.dis >= 0:
            sol1 = (-self.b + math.sqrt(self.dis))/2
            sol2 = (-self.b - math.sqrt(self.dis))/2

            print (f"\nel valor de la solución 1 es {sol1}\n")
            print (f"\nel valor de la solución 2 es {sol2}\n")

        else:
            print("\nla solucion a la equación introducida es un número complejo\n")

    def sollista(self):

        lista = []

        if self.dis >= 0:
            sol1 = (-self.b + math.sqrt(self.dis))/2
            sol2 = (-self.b - math.sqrt(self.dis))/2

        else:

            sol1 = "c1"
            sol2 = "c2"

        lista.append(sol1)
        lista.append(sol2)
        return lista

    def soltupla(self):

        tupla = []

        if self.dis >= 0:
            sol1 = (-self.b + math.sqrt(self.dis))/2
            sol2 = (-self.b - math.sqrt(self.dis))/2

        else:

            sol1 = "c1"
            sol2 = "c2"

        tupla.append(sol1)
        tupla.append(sol2)
        return tupla




eq = Eqsegundogrado(2, 4, 1)
    
eq.mostrar()
eq.redef()
eq.mostrar()
eq.resolver()