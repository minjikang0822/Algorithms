# self-balancing binary search tree
class AVLTree:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right
        self.height = 1
        self.balance = self.left.height - self.right.height

    def insert(self):
        pass

    def delete(self):
        pass

    def search(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
