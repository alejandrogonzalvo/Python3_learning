#!/usr/bin/python3.5
# -*- coding: utf-8 -*
"""Ejemplo aula:
Lista de numero aleatorio.
Las lista representa coeficientes ecuación segundo grado
"""
#para generar numeros aleatorios:
import random as r
#crear una lista:
miLista=[]

#añadir elementos a una lista:
miLista.append("cadena")
miLista.append(1)

miLista.append([1,2,3])
#mostrar contenido lista elemento a elemento:
indice=0
for ele in miLista:
    print("milista[{}]= {}".format(indice,ele))
    indice += 1

#genera un numero aleatorio entre 0 y 5
print (r.randint(0, 5))#La salida va a ser: 0, 1, 2, 3, 4 o 5


#crear una lista de tamaño n con los elementos que sean numeros aleatorios entre 0 y 1000
unaLista=[]
#ejercicio: hacer interactivo el tamaño de la lista? Es decir...
n=1000
for ele in range(0,n):
    #generar un numero aleatorio entre 0 y n elevado a 4
    ale=r.randint(0,n**4)
    #añadir el número generado a la lista
    unaLista.append(ale)
    #mostrar el indice y el contenido de ese índice
    print("ele= {0}: unaLista[{0}]= {1}".format(ele,ale))

#leer lista de tres en tres:
indice = 0
# variables para los coeficientes de la ecuación de segundo grado:
a=0
b=0
c=0

#para cada elemento de la lista procesar:
for indice in range(len(unaLista)):
    a=unaLista[indice]
    #aqui dará error cuando el resultado de la suma sea mayor que el numero
    #de elementos de la suma. Solucionar el problema
    #este es el "caso de estudio"
    b=unaLista[indice+1]
    c=unaLista[indice+2]
    #trabajo del alumno/a: aplicar el algoritmo la ecuación de segundo grado.
    
"""
Ejercicios:
1 Modificar el tamaño de la lista para que su tamaño siempre sea multiplo de tres.
  Sugerencias:
    a) antes de crear la lista comprobar si n es multiplo de 3, y actuar en consecuencia.
    b) para saber si un número es multipl de otro, usar la función resto
2 Modificar el proceso de lectura de la lista de tres en tres para que no se produza error:
  Sugerencias:
    a) usar try - except
    b) controlar con if's el valor del índice  
Prolemas nuevos:
    Modificar para guardar coeficientes  soluciones en una nueva lista. Cada elemento de la lista
    debe ser una lista con los coeficientes y soluciones o/y un diccionario con los mismos datos.
    Porcentaje de soluciones que:
        a) Tienen soluciones complejas
        b) Tiene una solución
        c) Tienen dos soluciones.
    
    
"""
