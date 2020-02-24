import csv


filename = "expenses.csv"

with open(filename) as f:
    text = csv.reader(f)
    
    for row in text:
        print(row)