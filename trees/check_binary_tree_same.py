class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


    def is_binary_tree_same(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        if root1.val != root2.val:
            return False;
        return self.is_binary_tree_same(root1.left, root2.left) and self.is_binary_tree_same(root1.right, root2.right)

if __name__=='__main__':
    root1 = Node(4)
    root1.left = Node(2)
    root1.right = Node(5)
    root1.left.left = Node(1)
    root1.left.right = Node(4)


    root2 = Node(4)
    root2.left = Node(2)
    root2.right = Node(5)
    root2.left.left = Node(1)
    root2.left.right = Node(4)


    print root1.is_binary_tree_same(root1, root2)
