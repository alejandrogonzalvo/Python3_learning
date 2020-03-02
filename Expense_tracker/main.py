"""

Expense_tracker: This program lets you create, edit, and save unlimited budgets.
The budgets are customizables by number of categories, initial amount of money,
name of each categorie and percentatge of money for each category.

You can record a spent on a specific category, or an earning, which will be 
automatically divided by the categories following the stablished criterium
by the user.

Made by Alejandro Gonzalvo
Github: https://github.com/dahko37/Python3_learning

"""


import os
import json


import money as m
import csv

def __str__(self):
   return "{0}".format(self.name)


def initialize(filename):
    """
    Adjusts the starting parameters.
    """

    budgets = []

    try: 
    # Checks if the file exists, and executes the apropiate code
    # according to the situation.
        with open(filename, 'r') as f_obj: 
            budgetslist = json.load(f_obj) 
            # Loads the info from older sessions 
            # into the list.
            for budget in budgetslist:
                oldacc = Account(
                    budget['name'],
                    budget['cash'],
                    budget['percent'],
                    budget['spends']
                    )
                budgets.append(oldacc)

    except FileNotFoundError: #If the file doesn't exist, we create it.
        print("Seems you are the first one here!")

    
    return budgets
     



class Account:
    """
    
    Simulates a budget with custom percentatges for each area of spending

    """
    def __init__(self, name, cash, percent, spends = []):
        self.name = name
        self.cash = int(cash)
        self.percent = percent
        self.budget = {}
        self.spends = spends

        for key, value in self.percent.items():
            self.budget[key] = self.cash * value / 100

        for spend in self.spends:
            for key, value in spend.items():
                self.budget[key] -= value



    def show(self):
        "shows actual budget"
        print(self.budget)


    def spend(self, amount, category):
        """Reduces the selected amount of money from the selected category"""
        if category in self.budget.keys() and amount < self.budget[category]:
            self.budget[category] -= amount
            spend = {category : amount}
            self.spends.append(spend)
             

        elif category in self.budget.keys():
            print("\nYou don't have enough money!\n")
            while True:
                res = input("Do you want to go red numbers? (Y/N) :  ")
                if res == "Y" or res == "y":
                    self.budget[category] -= amount
                    spend = {category : amount}
                    self.spends.append(spend)

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

        self.cash += amount
        for key, value in self.percent.items():
            self.budget[key] = self.cash * value / 100

        for spend in self.spends:
            for key, value in spend.items():
                self.budget[key] -= value
    
         


def getpath():
    """Returns the path of the file folder"""
    path = os.path.dirname(os.path.abspath(__file__))
    return path


def help():
    """Returns all the posible operations"""
    posop = [
        "help : Shows all posible operations" ,
        "create : Creates a new account" ,
        "select : Selects an existing account" , 
        "save : Saves the changesmade on the session" , 
        "spend : Records a spend on the selected account" , 
        "earn : Record an earning on the selected account" ,
        "exit : Closes the program"
    ]
    for op in sorted(posop):
        print("\n{0}\n".format(op))


def create():
    """creates a new account"""
    name = input("\nSelect name for new account: ")
    cash = int(input("Select inital amount of money: "))
    percent = {}
    
    while True:
        key = input("Name a new category: ")
        val = int(input("Select the percentatge (1-100): "))
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
            percent.clear()
            continue

    return name, cash, percent


def select(budgets):
    """Selects an existing account to work with"""
    budgetsname = []
    for budget in budgets:
        budgetname = __str__(budget)
        budgetsname.append(budgetname)
    
    print(budgetsname)
    accname = input("Select an existing account: ")
    
    if accname in budgetsname:

        ind = budgetsname.index(accname)
        print(budgets)
        selacc = budgets[ind]
        del budgets[ind]
        print(budgets)
        print('account succesfully changed')
        return selacc, budgets

    else:
        print("Sorry, the selected account doesn't exist")


def save(filename, budgets):
    """Saves the changes made into the accounts"""

    with open(filename, 'w') as f_obj:
        budgets2 = [budget.__dict__ for budget in budgets] 
        json.dump(budgets2, f_obj)
    


def main():
    """Executes the main program"""
    
    filename = "budgets.json"

    budgets = initialize(filename)

    while True:
        a = input("\nSelect the desired operation (h for help): ")

        if a == 'help':
            help()

        elif a == 'create':
            while True:
                accname, cash, percent = create()

                if accname in budgets:
                    print('\nSorry, there is already an account with this name. ')
                    continue

                break
            
            newacc = Account(accname, cash, percent)
            print('\nAccount created succesfully')
            budgets.append(newacc)

        elif a == 'select':
            try:
                budgets.append(selacc)

            except UnboundLocalError:
                pass

            selacc, budgets = select(budgets)
            
        elif a == 'show':
            selacc.show()

        elif a == 'earn':
            amount = int(input("\nHow much have you earned? : "))
            selacc.earn(amount)
            

        elif a == 'spend':
            amount = int(input("\nHow much have you spent? : " ))
            while True:
                category = input("On which category have you spent it? : ")
                
                if category in selacc.budget:
                    selacc.spend(amount, category)
                    break

                else:
                    print("\nThe selected category doesn't exist")


        elif a == 'save':
            try:
                budgets.append(selacc)
            
            except UnboundLocalError:
                pass
            
            save(filename, budgets)
            print('account saved succesfully')
        
        elif a == 'exit':
            try:
                budgets.append(selacc)
            
            except UnboundLocalError:
                pass
            save(filename, budgets)
            print('account saved succesfully')
            break

        else:
            print("ERROR: The input is not an operation\n")




