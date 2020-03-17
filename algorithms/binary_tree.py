import random as r


from node import Node


num_list = [r.randint(1, 1000) for _ in range(100)]
print(num_list)

root = Node()
for num in num_list:
    root.sort_val(num)

root.show_tree()
