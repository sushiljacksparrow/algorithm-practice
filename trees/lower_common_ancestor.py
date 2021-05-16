class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, root, key):
        if root.val > key:
            if root.left == None:
                root.left = Node(key)
            else:
                self.insert(root.left, key)
        else:
            if root.right == None:
                root.right = Node(key)
            else:
                self.insert(root.right, key)


    def lowest_common_ancestor(self, root, root1, root2):
        if root.val == root1.val or root.val == root2.val:
            return root

        if (root1.val <= root.val and root2.val > root.val) or (root2.val <= root.val and root1.val > root.val):
            return root

        elif root.val > max(root1.val, root2.val):
            return self.lowest_common_ancestor(root.left, root1, root2)
        else:
            return self.lowest_common_ancestor(root.right, root1, root2)



if __name__=='__main__':
    root = Node(10)
    root.insert(root, 5)
    root.insert(root, 6)
    root.insert(root, 1)
    root.insert(root, 3)
    root.insert(root, 20)
    root.insert(root, 25)

    print root.lowest_common_ancestor(root, Node(1), Node(3)).val
