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

    def delete(self, root, key):
        if root == None:
            return None
        if root.val > key:
            root.left = self.delete(root.left, key)
        elif root.val < key:
            root.right = self.delete(root.right, key)
        else:
            if root.left == None and root.right == None:
                root = None
            elif root.left == None:
                root.val = root.right.val
                root.left = None
            elif root.right == None:
                root.val = root.left.val
                root.right = None
            else:
                # find the minimum in right substree
                temp = root.right
                while temp.left != None:
                    temp = temp.left
                root.val = temp.val
                root.right = self.delete(root.right, temp.val)
        return root


    def print_in_order(self, root):
        if root != None:
            self.print_in_order(root.left)
            print root.val
            self.print_in_order(root.right)

    def print_pre_order(self, root):
        if root != None:
            print root.val
            self.print_pre_order(root.left)
            self.print_pre_order(root.right)

    def print_post_order(self, root):
        if root != None:
            self.print_post_order(root.left)
            self.print_post_order(root.right)
            print root.val

if __name__=='__main__':
    root = Node(10)
    root.insert(root, 5)
    root.insert(root, 20)
    root.insert(root, 25)
    root.insert(root, 1)
    root.insert(root, 3)
    root.insert(root, 6)


    print 'in order traversal of bst'
    root.print_in_order(root)

    print 'pre order traveral of bst'
    root.print_pre_order(root)

    print 'post order traversal of bst'
    root.print_post_order(root)


    root = root.delete(root, 5)
    print 'pre order after deleting'
    root.print_in_order(root)
