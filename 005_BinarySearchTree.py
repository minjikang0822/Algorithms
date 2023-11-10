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
            else:
                # case 2: node to delete has only one child
                if node_to_delete.left is not None:
                    node_to_delete.replace(node_to_delete.left, True)
                elif node_to_delete.right is not None:
                    node_to_delete.replace(node_to_delete.right, True)
                # case 3: no child
                else:
                    # 부모찾아서 none해야함
                    pass

    def printTree(self):
        # 수정 필요
        print(self.node)
        print(self.left.node, ' ', self.right.node)


def main():
    bst = BinarySearchTree(15)
    to_insert = [8, 24, 5, 13, 19, 28, 2, 6, 12, 25]
    for item in to_insert:
        bst.insert(item)
    bst.delete(11)
    bst.delete(24)
    bst.printTree()
    print(bst.left.right.left.node)


if __name__ == "__main__":
    main()
