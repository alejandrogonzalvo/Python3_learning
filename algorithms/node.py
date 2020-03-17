import random as r


class Node:
    """represents a node containing 1 or 0 values in a binary tree."""

    def __init__(self):
        self.left = None
        self.right = None
        self.val = None

    def insert(self, val):
        """Inserts the selected value in the correct node"""

        if self.val is None:
            self.val = val

        elif val < self.val:
            if self.left is None:
                self.left = Node()
            self.left.insert(val)

        elif val > self.val:
            if self.right is None:
                self.right = Node()
            self.right.insert(val)

    def show_tree(self):
        """Shows the value of the selected node and all its childs sorted."""
        if self.left:
            self.left.show_tree()
        print(self.val)
        if self.right:
            self.right.show_tree()

    def search(self,val):
        """Searches if the specified value is contained in the tree"""
        if self.left and val < self.val:
            s = self.left.search(val)

        elif val == self.val:
            print("{0} found in tree".format(val))
            s = True

        elif val > self.val and self.right:
            s = self.right.search(val)

        else:
            print("{0} NOT found in tree".format(val))
            s = False

        return s
