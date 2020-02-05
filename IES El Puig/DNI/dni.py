# Función para crear dni de forma automatizada.

# Las funciones calcletra y randletra son funciones creadas específicamente
# para la función principal, pero pueden ser usadas a gusto del usuario.

import datetime as d
import random as r


def creardni():
    """
    
    Crea un diccionario con la estructura de un dni con datos proporcionados
    por el usuario.
    
    """

    dni = {}

    dni["nombre"] = input("\nIntroduzca su nombre no completo: ")
    dni["apellido1"] = input("\n Introduzca su primer apellido: ")
    dni["apellido2"] = input("\n Introduzca su segundo apellido: ")

    dni["nacimiento"] = input("\n Introduzca su fecha de nacimiento (dd/mm/aaaa): ")

    dni["genero"] = input("\nIntroduzca F si es mujer M si es hombre: ")

    dni["nacionalidad"] = input("\nIntroduzca su nacionalidad: ")

    año = 2020
    mes = 2
    dia = 5
    fechacad = d.date(year = 10 + año, month = mes, day = dia)
    dni["fecha_caducidad"] = fechacad

    numero = r.randint(10000000, 99999999)
    letra = calcletra(numero)
    dni["codigo"] = str(numero) + letra

    l1 = randletra()
    l2 = randletra()
    l3 = randletra()
    numero = r.randint(100000, 999999)
    dni["numsoporte"] = l1 + l2 + l3 + str(numero)

    return dni



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
    
