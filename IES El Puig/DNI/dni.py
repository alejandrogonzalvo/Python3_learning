import datetime as d
import random as r


def dni():
    """
    
    Crea un diccionario con la estructura de un dni con datos proporcionados
    por el usuario.
    
    """

    dni = {}

    dni[nombre] = input("\nIntroduzca su nombre no completo: ")
    dni[apellido1] = input("\n Introduzca su primer apellido: ")
    dni[apellido2] = input("\n Introduzca su segundo apellido: ")

    dni[nacimiento] = input("\n Introduzca su fecha de nacimiento (dd/mm/aaaa): ")

    dni[genero] = input("\nIntroduzca F si es mujer M si es hombre: ")

    dni[nacionalidad] = input("\nIntroduzca su nacionalidad: ")

    hoy = d.now()
    dni[fecha_caducidad] = hoy + d.date(year = 10) 

    numero = r.randint(10000000, 99999999)
    letra = calcletra(numero)
    dni[codigo] = str(numero) + letra

    l1 = randletra()
    l2 = randletra()
    l3 = randletra()
    numero = r.randint(100000, 999999)
    dni[numsoporte] = 



def calcletra(numero):
    """
    
    Calcula una letra a partir de un numero dni, utilizando el mismo sistema
    que los dni reales.
    
    """
    
    i = numero % 23
    
    abecedario = [
                  "A" "B", "C", "D", "E",
                  "F", "G", "H", "I", "J",
                  "K", "L", "M", "N", "O",
                  "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y",
                  "Z"
                ]

    letra = abecedario[i]

    return letra


def randletra():
    """Devuelve una letra de forma pseudoaleatoria"""
    
    i = r.randint(0, 22)
    
    abecedario = [
                  "A" "B", "C", "D", "E",
                  "F", "G", "H", "I", "J",
                  "K", "L", "M", "N", "O",
                  "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y",
                  "Z"
                ]

    letra = abecedario[i]

    return letra
    
