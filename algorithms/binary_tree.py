import random as r


class node:
    """represents a node containing 1 or 0 values in a binary tree."""

    def __init__(self):
        self.left = None
        self.right = None
        self.val = None 

    def sort_val(self, val):
        """Inserts the selected value in the correct node"""

        if self.val == None:
            self.val = val

        elif val < self.val:
            self.left = node()
            self.left.sort_val(val)

        elif val == self.val:
            pass

        elif val > self.val:
            self.right = node()
            self.right.sort_val(val)

    def show_tree(self):
        """Shows the value of the selected node and all its childs sorted."""

        if self.left != None:
            self.left.show_tree()

        if self.right != None:
            self.right.show_tree()

        if self.val != None:
            print(self.val)


numlist = []

for i in range(100):
    i = r.randint(1,1000)
    numlist.append(i)

print(numlist)

root = node()

for num in numlist:
    root.sort_val(num)

root.show_tree()



