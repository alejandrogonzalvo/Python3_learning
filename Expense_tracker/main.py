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

        budgetsname = []
        for budget in budgets:
            budgetname = __str__(budget)
            budgetsname.append(budgetname)

    except FileNotFoundError: #If the file doesn't exist, we create it.
        print("Seems you are the first one here!")
        budgetslist = []
        budgetsname = []

    
    return budgets, budgetslist, budgetsname
     

def getpath():
    """Returns the path of the file folder"""
    path = os.path.dirname(os.path.abspath(__file__))
    return path


def help():
    """Returns all the posible operations"""
    posop = [
        "help : Shows all posible operations" ,
        "show : Shows all information about selected account"
        "create : Creates a new account" ,
        "select : Selects an existing account" , 
        "spend : Records a spend on the selected account" , 
        "earn : Record an earning on the selected account" ,
        "exit : Closes the program"
    ]
    for op in sorted(posop):
        print("\n{0}\n".format(op))


def create():
    """creates a new account"""
    
    name = input("\nSelect name for new account: ")
    while True:
        try:
            cash = int(input("\nSelect inital amount of money: "))
        except ValueError:
            print("\nERROR: MONEY IS A NUMBER, NOT A WORD")
            continue
        
        break
    percent = {}
    
    while True:
        key = input("Name a new category: ")
        while True:
            try:
                val = int(input("Select the percentatge (1-100): "))
            except ValueError:
                print("\nERROR: PERCENTATGE IS A NUMBER, NOT A WORD")
                continue
            break
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


def select(budgets, budgetsname):
    """Selects an existing account to work with"""
    
    print("\n{0}".format(budgetsname))
    accname = input("\nSelect an existing account: ")
    
    if accname in budgetsname:

        ind = budgetsname.index(accname)
        selacc = budgets.pop(ind)
        print('account succesfully changed')
        return selacc, budgets

    else:
        print("\nSorry, the selected account doesn't exist")


def save(filename, budgets):
    """Saves the changes made into the accounts"""

    with open(filename, 'w') as f_obj:
        budgetslist = [budget.__dict__ for budget in budgets] 
        json.dump(budgetslist, f_obj)
    


def main():
    """Executes the main program"""
    
    filename = "budgets.json"

    budgets, budgetslist, budgetsname = initialize(filename)

    while True:
        a = input("\nSelect the desired operation (h for help): ")

        if a == 'help':
            help()

        elif a == 'create':
            while True:
                accname, cash, percent = create()

                if accname in budgetsname:
                    print('\nSorry, there is an account with this name. ')
                    continue

                break
            
            newacc = Account(accname, cash, percent)
            acclist = newacc.__dict__
            budgetname = __str__(newacc.name)
            print('\nAccount created succesfully')
            budgets.append(newacc)
            budgetslist.append(acclist)
            budgetsname.append(budgetname)

        elif a == 'select':
            try:
                budgets.append(selacc)

            except UnboundLocalError:
                pass
            
            try:
                selacc, budgets = select(budgets, budgetsname)
            
            except TypeError:
                try:
                    budgets.remove(selacc)

                except UnboundLocalError:
                    pass
            
        elif a == 'show':
            try:
                selacc.show()
            except UnboundLocalError:
                print("\nERROR: NO ACCOUNT SELECTED")

        elif a == 'earn':
            amount = int(input("\nHow much have you earned? : "))
            selacc.earn(amount)

        elif a == 'spend':
            amount = int(input("\nHow much have you spent? : " ))
            while True:
                category = input("\nIn which category have you spent it? : ")
                
                if category in selacc.budget:
                    selacc.spend(amount, category)
                    break

                else:
                    print("\nThe selected category doesn't exist")
        
        elif a == 'exit':
            try:
                budgets.append(selacc)
            
            except UnboundLocalError:
                pass
            save(filename, budgets)
            print('\nAccount saved succesfully')
            break

        else:
            print("\nERROR: THE INPUT IS NOT A POSSIBLE OPERATION")




