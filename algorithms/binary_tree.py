import random as r


from nodes import Binode


num_list = [r.randint(1, 1000) for _ in range(1000)]
print(num_list)

root = Binode()
for num in num_list:
    root.insert(num)

root.show_tree()
a = root.search(900)
b = root.search(100)
c = root.search(2000)

print(a)
print(b)
print(c)
