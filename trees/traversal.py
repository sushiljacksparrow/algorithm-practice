class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


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
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print 'in order traveral'
    root.print_in_order(root)

    print 'pre order traversal'
    root.print_pre_order(root)


    print 'post order traversal'
    root.print_post_order(root)
