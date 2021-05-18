import math
prev = -9999999

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


    def check_bst(self, root):
        global prev
        if root != None:
            if not self.check_bst(root.left):
                return False

            if root.val < prev:
                return False

            prev = root.val

            return self.check_bst(root.right)

        return True


if __name__=='__main__':
    root = Node(10)
    root.left = Node(3)
    root.right = Node(50)

    print root.check_bst(root)
