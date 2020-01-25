# !/usr/bin/python3.5


class Eqsegundogrado:
    """

    Estructura de datos con formato de equación de segundo grado y funciones
    de interacción con sus respectivos algoritmos.
    
    """


    def __init__(self, a = 0, b = 0, c = 0):
        """

        Asignamos valores, y mostramos la equación actual.

        """

        self.a = a
        print (f"\nel valor de a es {self.a}")

        self.b = b
        print (f"\nel valor de b es {self.b}")

        self.c = c
        print (f"\nel valor de c es {self.c}")

        self.dis = self.b*self.b-4*self.a*self.c

        self.sol1 = (-self.b + self.dis**0.5)/2
        self.sol2 = (-self.b - self.dis**0.5)/2

        self.eq = f"{self.a}x*x + {self.b}x + {self.c}"



        print(f"\n{self.eq} es la nueva equación")


    def __str__(self):
        """

        Contenido cuando hagamos print() a un objeto de clase Eqsegundogrado.

        """

        return f'{self.eq} es la equación actual'.format(self=self)


    def redef(self):
        """
        
        Recopila el valor de las variables de la equacion
        
        """

        self.a = int(input("introduzca el nuevo valor de la variable a:"))
        print (f"el valor de a es {self.a}")

        self.b = int(input("introduzca el nuevo valor de la variable b:"))
        print (f"el valor de a es {self.b}")

        self.c = int(input("introduzca el nuevo valor de la variable c:"))
        print (f"el valor de a es {self.c}")

        print(f"{self.eq} es la nueva equación")


    def tiposol(self):
        """

        Devuelve el tipo de solución.

        """

        if self.dis > 0:
            print("La equacion tiene dos soluciones reales.")

        elif self.dis == 0:
            print("La equacion solo tiene una solucion real (0).")

        else:
            print("La equacion tiene 2 soluciones imaginarias.")


    def mostrarsol(self):
        """

        Muestra las soluciones de la equación.

        """

        print (f"\nel valor de la solución 1 es {self.sol1}\n")
        print (f"\nel valor de la solución 2 es {self.sol2}\n")


    def sollista(self):
        """

        Devuelve las soluciones como una lista

        """

        lista = [self.sol1, self.sol2]

        return lista


    def soltupla(self):
        """

        Devuelve las soluciones como una tupla

        """

        tupla = (self.sol1, self.sol2)

        return tupla




eq = Eqsegundogrado(8, 4, 1)
    
print(eq)
eq.redef()
print(eq)
eq.mostrarsol()