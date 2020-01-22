#!/usr/bin/python3.5
# -*- coding: utf-8 -*
"""Ejemplo aula:
Lista de numero aleatorio.
Las lista representa coeficientes ecuación segundo grado
"""
#para generar numeros aleatorios:
import random as r
#para hacer operaciones a nivel de sistema operativo
import os

#crear una lista de tamaño n con los elementos que sean numeros aleatorios entre 0 y 1000
unaLista=[]
"""
Ejercicios:
1 Modificar el tamaño de la lista para que su tamaño siempre sea multiplo de tres.
  Sugerencias:
    a) antes de crear la lista comprobar si n es multiplo de 3, y actuar en consecuencia.
    b) para saber si un número es multipl de otro, usar la función resto
"""
mensaje="""Introducir el número de elementos que debe tener la lista.
Debe ser un número positivo, entero  y multiplo de 3.
"""
while (1):
    #borrar la pantalla
    os.system("clear")
    print(mensaje)
    #pedir el valor de n
    try:
        n=abs(int(input("Valor de n: ")))
    except ValueError:
        mensaje="Tipo de dato incorrecto. Solo valores numéricos enteros, please!!"
        print(mensaje)
        continue
    if (n % 3 == 0): break
    if (n % 3 == 1): n = n + 2; break;
    if (n % 3 == 2): n = n + 1; break;
    
mensaje="""el numero de elementos que va a tener la list es {} que es multiplo de 3
"""
print(mensaje.format(n))

#cargar lista con números aleatorios.
for ele in range(0,n):
    #generar un numero aleatorio entre 0 y n elevado a 4
    ale=r.randint(0,n**4)
    #añadir el número generado a la lista
    unaLista.append(ale)
    #mostrar el indice y el contenido de ese índice
    #print("ele= {0}: unaLista[{0}]= {1}".format(ele,ale))

#leer lista de tres en tres:
indice = 0
# variables para los coeficientes de la ecuación de segundo grado:
a=0
b=0
c=0
"""
2 Modificar el proceso de lectura de la lista de tres en tres para que no se produza error:
  Sugerencias:
    a) usar try - except
    b) controlar con if's el valor del índice
    Pero la mejor solución y la mas sencilla es usar las posibilidades de range.
"""

#ahora estamos seguros de que la lista tiene un numero de elementos multiplos de 3
#para cada elemento de la lista procesar:
for indice in range(0,len(unaLista),3):
    a=unaLista[indice]
    b=unaLista[indice+1]
    c=unaLista[indice+2]
    print("indice: {}".format(indice))
    print("\t\ta: {}, b: {}, c: {}".format(a,b,c))
    #trabajo del alumno/a: aplicar el algoritmo la ecuación de segundo grado.
    
"""
Prolemas nuevos:
    Modificar para guardar coeficientes  soluciones en una nueva lista. Cada elemento de la lista
    debe ser una lista con los coeficientes y soluciones o/y un diccionario con los mismos datos.
    Porcentaje de soluciones que:
        a) Tienen soluciones complejas
        b) Tiene una solución
        c) Tienen dos soluciones.
     
"""

