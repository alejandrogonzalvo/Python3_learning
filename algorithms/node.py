class Node:
    """represents a Node containing 1 or 0 values in a binary tree."""

    def __init__(self):
        self.left = None
        self.right = None
        self.val = None

    def sort_val(self, val):
        """Inserts the selected value in the correct Node"""

        if self.val == None:
            self.val = val

        elif val < self.val:
            if self.left is None:
                self.left = Node()
            self.left.sort_val(val)

        elif val == self.val:
            pass

        elif val > self.val:
            if self.left is None:
                self.right = Node()
            self.right.sort_val(val)

    def show_tree(self):
        """Shows the value of the selected Node and all its childs sorted."""

        if self.left:
            self.left.show_tree()

        print(self.val)


        if self.right:
            self.right.show_tree()
