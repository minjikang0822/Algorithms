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
        print(self.node)
        if self.left is not None:
            self.left.preOrderTraverse()
        if self.right is not None:
            self.right.preOrderTraverse()


def main():
    bst = BinarySearchTree('A', BinarySearchTree('B', 'D', 'E'), BinarySearchTree('C', 'F', 'G'))
    bst.preOrderTraverse()
    print("---")


if __name__ == "__main__":
    main()