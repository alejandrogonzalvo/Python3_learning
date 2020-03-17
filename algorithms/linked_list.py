from nodes import Linode


e0 = Linode(5)
e0.add(8)
e1 = e0.next
print(e0.val, e1.val)
e0.show_list()
