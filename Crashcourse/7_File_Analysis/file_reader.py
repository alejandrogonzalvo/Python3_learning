# !/usr/bin/python3.5

# Reads a file and prints its contents.


filename = 'txt\pi.txt'

with open(filename) as file_object:
    cont = file_object.read()
    print(cont)