import os
import json


import money as m
import csv


def initialize(filename):
    """
    Adjusts the starting parameters.
    """

    budgets = []

    try: 
    # Checks if the file exists, and executes the apropiate code
    # according to the situation.
        with open(filename, 'r') as f_obj: 
            budgets = json.load(f_obj) 
            # Loads the info from older sessions 
            # into the list.

    except FileNotFoundError: #If the file doesn't exist, we create it.
        print("Seems you are the first one here!")

        with open(filename, 'w') as f_obj:
            pass

        return budgets
     



class Account:
    """
    
    Simulates a budget with custom percentatges for each area of spending

    """
    def __init__(self, name, cash = "0", percent):
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
    name = input("\nSelect name for new account: ")
    cash = input("Select inital amount of money: ")
    percent = {}
    
    while True:
        key = input("Name a new category")
        val = input("Select the percentatge (1-100) for the new category")
        percent[key] = val
        total_val = 0

        for val in percent.values():
            total_val += val

        if total_val < 100:
            print("The percentatge is smaller than 100. Add a new category")
            continue

        elif total_val == 100:
            print("The percentatge is = to 100. Creating budget")
            break

        elif total_val > 100:
            print("The percentatge cannot be greater than 100. Restarting")
            total_val = 0


def main():
    """Executes the main program"""
    
    filename = "budgets.json"

    budgets = initialize(filename)

    while True:
        a = input("Select the desired operation (h for help): ")

        if a == 'h':
            help()

        elif a == 'z':
            break

        elif a == 's':

        else:
            print("ERROR: The input is not an operation\n")




