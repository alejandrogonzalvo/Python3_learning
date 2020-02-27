import os


import money as m
import csv


class Account:
    """
    
    Simulates a budget with custom percentatges for each area of spending

    """
    def __init__(self, name, cash, percent):
        self.name = name
        self.cash = cash
        self.percent = percent
        self.budget = {}
            
        for key, value in self.percent.items():
            self.budget[key] = self.cash * value / 100


    def show(self):
        "shows actual budget"
        print(self.budget)


    def spend(self, amount, category):
        """Reduces the selected amount of money from the selected category"""
        if category in self.budget.keys() and amount < self.budget[category]:
            self.budget[category] -= amount

        elif category in self.budget.keys():
            print("\nYou don't have enough money!\n")
            while True:
                res = input("Do you want to go red numbers? (Y/N) :  ")
                if res == "Y" or res == "y":
                    self.budget[category] -= amount
                    break

                if res == "N" or res == "n":
                    print("Good decision! Operation canceled :)")
                    break
              
        else:
            print("\nthe selected category doesn't exist")
            
        


    def earn(self, amount):
        """
        
        Generates the selected amount of money and divides it
        following the percentatges.
        
        """
        for key, value in self.percent.items():
            self.budget[key] = amount * value / 100
    
         


def getpath():
    """Returns the path of the file folder"""
    path = os.path.dirname(os.path.abspath(__file__))
    return path


def help():
    """Returns all the posible operations"""
    print(
        "Possible operations:\n\n" +
        "h (help): shows all posible operations\n" +
        "s (show): shows all information about the selected account"
    )


def create():
    """creates a new account"""


        

def show(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def main():
    while True:
        a = input("Select the desired operation (h for help): ")

        if a == 'h':
            help()

        elif a == 'z':
            break

        elif a == 's':
            try:
                show(filename)
            except NameError:
                print("No account has been selected. " +
                "Please select an existing account or create a new one")
        else:
            print("ERROR: The input is not an operation\n")




