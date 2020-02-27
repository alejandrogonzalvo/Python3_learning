import os


import money as m
import csv


def getpath():
    """Returns the path of the file folder"""
    path = os.path.dirname(os.path.abspath(__file__))
    return path


def help():
    print(
        "Possible operations:\n\n" +
        ""
    )


def show(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def main():
    path = getpath()
    filename = path + "/expenses.csv"

    while True:
        a = input("Select the desired operation (h for help): ")

        if a == 'h':
            help()

        elif a == 'z':
            break

        elif a == 's':
            show(filename)
        else:
            print("ERROR: The input is not an operation\n")




