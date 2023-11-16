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
                return self.right.search(item)
            else:
                print(item, " doesn't exist")
                return None
        elif self.node > item:
            if self.left is not None:
                return self.left.search(item)
            else:
                print(item, " doesn't exist")
                return None

    def replace(self, to_replace, replace_children):
        self.node = to_replace.node
        if replace_children:
            self.right = to_replace.right if to_replace.right is not None else None
            self.left = to_replace.left if to_replace.left is not None else None

    def deleteLeaf(self, item):
        if self.node < item:
            if self.right is not None:
                if self.right.node == item:
                    self.right = None
                    print(item, " deleted")
                else:
                    self.right.deleteLeaf(item)
        elif self.node > item:
            if self.left is not None:
                if self.left.node == item:
                    self.left = None
                    print(item,  "deleted")
                else:
                    self.left.deleteLeaf(item)

    def delete(self, item):
        node_to_delete = self.search(item)
        if node_to_delete is not None:
            # case 1: node to delete has two children
            if node_to_delete.left is not None and node_to_delete.right is not None:
                parent = node_to_delete
                temp = node_to_delete.right
                cnt = 0
                while temp.left is not None:
                    cnt += 1
                    parent = temp
                    temp = temp.left
                node_to_delete.replace(temp, False)
                if cnt != 0:
                    parent.left = None
                elif cnt == 0:
                    parent.right = None
                    # case 3: no child
            elif node_to_delete.left is None and node_to_delete.right is None:
                self.deleteLeaf(item)
            else:
                # case 2: node to delete has only one child
                if node_to_delete.left is not None:
                    node_to_delete.replace(node_to_delete.left, True)
                elif node_to_delete.right is not None:
                    node_to_delete.replace(node_to_delete.right, True)

    def printTree(self):
        # 수정 필요
        # print(self.node)
        if self.left is None and self.right is not None:
            print("None  ", self.right.node)
            self.right.printTree()
        elif self.right is None and self.left is not None:
            print(self.left.node, "  None")
            self.left.printTree()
        elif self.left is not None and self.right is not None:
            print(self.left.node, "  ", self.right.node)
            self.left.printTree()
            self.right.printTree()
        print("----------------")

    def printTree2(self):
        # 수정 필요
        # print(self.node)
        if self.left is None and self.right is not None:
            print("None  ", self.right.node)
            self.right.printTree2()
        elif self.right is None and self.left is not None:
            print(self.left.node, "  None")
            self.left.printTree2()
        elif self.left is not None and self.right is not None:
            print(self.left.node, "  ", self.right.node)
            self.left.printTree2()
            self.right.printTree2()
        print("---------")


def main():
    bst = BinarySearchTree(15)
    to_insert = [8, 24, 5, 11, 19, 28, 2, 6, 13, 25, 12]
    for item in to_insert:
        bst.insert(item)
    # bst.delete(11)
    bst.delete(12)
    # bst.delete(24)
    # bst.printTree2()
    print(bst.left.right.right.node)


if __name__ == "__main__":
    main()
