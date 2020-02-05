# !/usr/bin/python3.5

# This program reads from a .txt file that contains the pi number and searches the given number inside.


filename = 'txt\pi_billion'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first billion digits of pi!")

else:
    print("Your birthday does not appear in the first billion digits of pi!")