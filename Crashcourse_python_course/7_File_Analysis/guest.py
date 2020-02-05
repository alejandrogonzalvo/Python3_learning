# !/usr/bin/python3.5


filename = 'txt\guest_book.txt'

while True:
    with open(filename, 'a') as f_obj:
        name = input("Whats your name?")
        f_obj.write( name + '\n')
        print("welcome yo the party, " + name + "!")