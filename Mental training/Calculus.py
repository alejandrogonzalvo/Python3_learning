# !/usr/bin/python3.5


import random as r
import sys


def gameover():
    """ Ends the game when the player gets out of lives """

    print("\n Oh, you lost all your lives, better luck next time! :( ")
    sys.exit()


def sum(lives):
    """Generates a random sum to solve with limited tries."""

    a = r.randint(1, 99)
    b = r.randint(1, 99)

    while lives > 0:

        psol = int(input(f"\n{a} + {b} = ")) # Player solution.
        csol = a + b                         # Correct solution.
        print(csol)

        if psol == csol:
            print("\nCorrect!")

            break

        else:
            lives += -1
            print(f"\nWrong! {lives} tries remaining.")


    if lives == 0:
        gameover()


def substraction(lives):
    """Generates a random substraction to solve with limited tries."""

    a = r.randint(1, 99)
    b = r.randint(1, 99)

    while lives > 0:

        if a > b:
            psol = int(input(f"\n{a} - {b} = ")) # Player solution.
            csol = a - b                         # Correct solution.
            print(csol)

        if b > a:
            psol = int(input(f"\n{b} - {a} = ")) # Player solution.
            csol = b - a                         # Correct solution.
            print(csol)


        if psol == csol:
            print("\nCorrect!")

            break

        else:
            lives += -1
            print(f"\nWrong! {lives} tries remaining.")

        
        if lives == 0:
            gameover()


def multiplication(lives):
    """Generates a random multiplication to solve with limited tries."""

    a = r.randint(1, 10)
    b = r.randint(1, 10)
    
    while lives > 0:

        psol = int(input(f"\n{a} x {b} = ")) # Player solution.
        csol = a * b                         # Correct solution.
        print(csol)

        if psol == csol:
            print("\nCorrect!")

            break

        else:
            lives += -1
            print(f"\nWrong! {lives} tries remaining.")

    if lives == 0:
        gameover()


def division(lives):
    """Generates a random division to solve with limited tries."""

    a = r.randint(50, 100)
    b = r.randint(1, 10)

    while a % b != 0:
        a = r.randint(50, 100)
        b = r.randint(2, 10)

    while lives > 0:

        psol = int(input(f"\n{a} : {b} = ")) # Player solution.
        csol = a / b                         # Correct solution.
        print(csol)

        if psol == csol:
            print("\nCorrect!")

            break

        else:
            lives += -1
            print(f"\nWrong! {lives} tries remaining.")

    if lives == 0:
        gameover()




def game(lives):
    """Mental calculus game"""
    
    for i in range(3):

        sum(lives)

    for i in range(3): 
        
        substraction(lives)

    for i in range(3):
        
        multiplication(lives)

    for i in range(3):
        
        division(lives) 

    print("\nCongratulations, you won!")



game(5)




