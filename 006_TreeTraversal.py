class BinarySearchTree:
    def __init__(self, root=None, left=None, right=None):
        self.node = root
        if type(left) is BinarySearchTree:
            self.left = left
        else:
            self.left = BinarySearchTree(left) if left is not None else None
        if type(right) is BinarySearchTree:
            self.right = right
        else:
            self.right = BinarySearchTree(right) if right is not None else None

    def preOrderTraverse(self):
        # parent -> left -> right
        print(self.node, end=" ")
        if self.left is not None:
            self.left.preOrderTraverse()
        if self.right is not None:
            self.right.preOrderTraverse()

    def inOrderTraverse(self):
        if self.left is not None:
            self.left.inOrderTraverse()
        print(self.node, end=" ")
        if self.right is not None:
            self.right.inOrderTraverse()

    def postOrderTraverse(self):
        if self.left is not None:
            self.left.postOrderTraverse()
        if self.right is not None:
            self.right.postOrderTraverse()
        print(self.node, end=" ")


def main():
    bst = BinarySearchTree('A', BinarySearchTree('B', 'D', 'E'), BinarySearchTree('C', 'F', 'G'))
    bst.preOrderTraverse()
    print()
    bst.inOrderTraverse()
    print()
    bst.postOrderTraverse()


if __name__ == "__main__":
    main()