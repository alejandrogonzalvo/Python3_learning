import random as r


from node import Node


numlist = []

for i in range(100):
    i = r.randint(1,1000)
    numlist.append(i)

print(numlist)

root = Node()

for num in numlist:
    root.sort_val(num)

root.show_tree()
