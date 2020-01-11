# !/usr/bin/python3.5


filename = 'txt\pi.txt'

with open(filename) as file_object:
    cont = file_object.read()
    print(cont)