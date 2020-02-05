# !/usr/bin/python3.5


def welcome_magicians(magician_list):
    for magician in magician_list:
        print('\nLadies and gentlemen, welcome to ' + str(magician.title()) + "'s show!")

def greatizinator(magician_list):
    index = 0
    for magician in magician_list:
        magician = 'the great ' + magician
        magician_list[index] = magician
        index += 1
    return magician_list

magicians = ['houdini', 'rasputin', 'stravinski']
magicians = greatizinator(magicians)
welcome_magicians(magicians)
