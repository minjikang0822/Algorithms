class BinarySearchTree:
    def __init__(self, node=None):
        self.node = node
        self.left = None
        self.right = None

    def insert(self, item):
        if self.node is None:
            self.node = item
        elif self.node < item:
            if self.right is not None:
                self.right.insert(item)
            else:
                self.right = BinarySearchTree(item)
        else:
            if self.left is not None:
                self.left.insert(item)
            else:
                self.left = BinarySearchTree(item)

    def search(self, item):
        if self.node == item:
            print(self.node, " found")
            return self
        elif self.node < item:
            if self.right is not None:
                self.right.search(item)
            else:
                print(item, " doesn't exist")
                return None
        elif self.node > item:
            if self.left is not None:
                self.left.search(item)
            else:
                print(item, " doesn't exist")
                return None

    def delete(self, item):
        node_to_delete = self.search(item)
        print("hi", self.node)
        if node_to_delete is not None:
            # case 1: node to delete has two children
            if node_to_delete.left is not None and node_to_delete.right is not None:
                node_to_replace = node_to_delete.right
                # node to replace doesn't have a left child
                if node_to_replace.left is None:
                    node_to_delete.node = node_to_replace
                else:
                    while node_to_replace.left is not None:
                        temp_parent = node_to_replace
                        node_to_replace = node_to_replace.left
                        if node_to_replace.left is None:
                            # delete the node to replace from the tree
                            temp_parent.left = None
                    node_to_delete.node = node_to_replace.node
            else:
                # case 2: node to delete has only one child
                if node_to_delete.left is not None:
                    node_to_delete.node = node_to_delete.left
                # if right child is not None
                else:
                    node_to_delete.node = node_to_delete.right

    def printTree(self):
        print(self.node)
        print(self.left.node, ' ', self.right.node)


def main():
    bst = BinarySearchTree(15)
    to_insert = [8, 24, 5, 11, 2, 6, 13, 12, 19, 25, 28]
    for item in to_insert:
        bst.insert(item)
    bst.delete(11)
    bst.delete(24)
    bst.printTree()
    print(bst.right.node)


if __name__ == "__main__":
    main()
