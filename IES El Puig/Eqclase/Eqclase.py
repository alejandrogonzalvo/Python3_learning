# !/usr/bin/python3.5


import math
import time


class Eqsegundogrado():
    """Estructura de datos con formato de equación de segundo grado y funciones de interacción con sus respectivos algoritmos."""


    def __init__(self):

        self.a = int(input("introduzca el nuevo valor de la variable a:"))
        print (f"el valor de a es {self.a}")

        self.b = int(input("introduzca el nuevo valor de la variable b:"))
        print (f"el valor de a es {self.b}")

        self.c = int(input("introduzca el nuevo valor de la variable c:"))
        print (f"el valor de a es {self.c}")

        print(f"\n{self.a}x*x + {self.b}x + {self.c} es la nueva equación")


    def mostrar(self):
        print(f"\n{self.a}x*x + {self.b}x + {self.c} es la equación actual")


    def redef(self):
        """Recopila el valor de las variables de la equacion"""

        self.a = int(input("introduzca el nuevo valor de la variable a:"))
        print (f"el valor de a es {self.a}")

        self.b = int(input("introduzca el nuevo valor de la variable b:"))
        print (f"el valor de a es {self.b}")

        self.c = int(input("introduzca el nuevo valor de la variable c:"))
        print (f"el valor de a es {self.c}")

        print(f"{self.a}x*x + {self.b}x + {self.c} es la nueva equación")

    def resolver(self):
        dis = self.b*self.b-4*self.a*self.c
    
        if dis >= 0:
            sol1 = (-self.b + math.sqrt(self.b*self.b -4*self.a*self.c))/2
            sol2 = (-self.b + math.sqrt(self.b*self.b -4*self.a*self.c))/2

            print (f"\nel valor de la solución 1 es {sol1}\n")
            print (f"\nel valor de la solución 2 es {sol2}\n")

        else:
            print("\nla solucion a la equación introducida es un número complejo\n")


eq = Eqsegundogrado()
    
eq.mostrar()
eq.redef()
eq.mostrar()
eq.resolver()