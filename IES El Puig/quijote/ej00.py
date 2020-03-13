#!/usr/bin/python3.5
# -*- coding: utf-8 -*-2
import string # para manipulación de datos string
import re # para usar expresiones regulares
import csv # para manipulacion de archivos csv

patron=re.compile(r'\W+') # Convierte la expresión regular en un objeto, para poder buscarlo más adelante. 
frqLetras={}
f = open ('/home/alejandrogonzalvo4eso/Escritorio/python3_learning/IES El Puig/quijote/pg2000.txt','r') # abre el archivo pasado como parametro
mensaje = f.read() # convierte el archivo en un objeto python manipulable (un string en este caso).
palabras = patron.split(mensaje) # Convierte el string mensaje en una lista, separando cada elemento al encontrarse con la expresion regular contenida en el patron.
for i in mensaje: # Para cada elemento de la lista, sienda cada elemento en este caso un caracter.
    ileida = i.lower()# Crea una copia del elemento con todas las letras minúsculas.
    if (ileida in string.ascii_lowercase): # Si el caracter es una letra del abecedario.
        if (ileida in frqLetras): # Si la letra se encuetra en letras frecuencia de letras.
            frqLetras[ileida] +=1 # Aumentamos la frecuencia en uno
        else:
            frqLetras[ileida]  =1 # Añadimos la letra a las letras que aparecen y establecemos su valor inicial en uno.
f.close() # Como no necesitamos manipular mas el archivo lo cerramos.
for k,v in frqLetras.items(): # Para clave, valor en cada elemento del diccionario
    print(k," : ",v) # Imprime la letra, y las veces que aparece cada letra.
    
print(palabras, len(palabras)) # Imprime la lista palabras, y indica los elementos que contiene 
print(palabras.sort()) # Ordena las palabras alfabeticamente y las imprime.


filename = "info.csv"

with open(filename, 'w') as f: 
    infowriter = csv.writer(f)

    for k,v in frqLetras.items():
        infowriter.writerow(f"{k} : {v}")

    infowriter.writerow(palabras)

