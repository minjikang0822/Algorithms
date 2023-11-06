class Tree:
    def __init__(self, node=None):
        self.node = node
        self.left = None
        self.right = None
        self.size = 1 if node is not None else 0

    def height(self):
        cnt = 0
        temp_size = 0
        while self.size > temp_size:
            temp_size += 2 ** cnt
            cnt += 1
        return cnt

    def insert(self, item):
        left = self.left
        right = self.right

        while left is not None and right is not None:
            left = left.left
            right = right.right

        if left is None:
            left = Tree(item)
        else:
            right = Tree(item)

        '''if self.left is None:
            self.left = Tree(item)
            return True
        elif self.right is None:
            self.right = Tree(item)
            return True
        else:
            while self.left.insert(item) or self.right.insert(item):
                return False'''

    def printTree(self):
        print(self.node)
        if self.left is not None:
            print("left")
            self.left.printTree()
        if self.right is not None:
            print("right")
            self.right.printTree()


        '''while left is not None and right is not None:
            print(self.node)
            print("/ \\")
            print(left.node, " ", right.node)
            left = left.left
            right = right.right

        if left is not None and right is None:
            print("/")
            print(left.node)'''


tree = Tree(3)
tree.insert(1)
tree.insert(2)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(9)
tree.printTree()
