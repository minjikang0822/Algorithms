from collections import deque

# self-balancing binary search tree
class AVLTree:
    def __init__(self, node, left=None, right=None):
        self.root = self
        self.node = node
        self.left = left
        self.right = right
        self.height = 0
        self.depth = 0

    def balance(self):
        balanceFactor = self.left.height - self.right.height
        return balanceFactor

    def insert(self, newData):
        crr = self
        newNode = AVLTree(newData)
        newNode.height = 0
        is_leaf = False
        while True:
            if crr.node < newData:
                if crr.right is None:
                    if crr.left is None:
                        is_leaf = True
                    crr.right = newNode
                    break
                crr = crr.right
            else:
                if crr.left is None:
                    if crr.right is None:
                        is_leaf = True
                    crr.left = newNode
                    break
                crr = crr.left
        newNode.depth = crr.depth + 1
        if is_leaf:
            self.re_calculate_height(newNode)

    def re_calculate_height(self, newNode):
        crr = self
        root_height = 0
        newData = newNode.node
        while crr is not newNode:
            if crr is not self.root:
                crr.height += 1
            root_height += 1
            if crr.node > newData:
                crr = crr.left
            else:
                crr = crr.right
        if self.root.height < root_height:
            self.root.height = root_height

    def printTree(self):
        tree_height = self.root.height
        temp_list = [[] for _ in range(tree_height + 1)]
        branch_list = [[] for _ in range(tree_height + 1)]
        temp_list[0] = [str(self.root.node)]
        done = []
        queue = deque([self.root])
        while queue:
            crr = queue.popleft()
            if crr in done:
                continue
            next_depth = crr.depth + 1
            if next_depth > tree_height:
                continue
            if crr.left is not None:
                queue.append(crr.left)
                temp_list[next_depth].append(str(crr.left.node))
                branch_list[next_depth-1].append('/')
            else:
                temp_list[next_depth].append('#')
                branch_list[next_depth-1].append(' ')

            if crr.right is not None:
                queue.append(crr.right)
                temp_list[next_depth].append(str(crr.right.node))
                branch_list[next_depth-1].append('\\')
            else:
                temp_list[next_depth].append('#')
                branch_list[next_depth-1].append('')
            done.append(crr)

        for i in range(len(temp_list)):
            n = 3*tree_height-i
            m = 3*tree_height-i
            print('*'*n, '  '.join(temp_list[i]))
            print('*'*m, ' '.join(branch_list[i]))

    def delete(self):
        pass

    def search(self):
        pass


def main():
    test_tree = AVLTree(10)
    test_tree.insert(2)
    test_tree.insert(5)
    test_tree.insert(11)
    test_tree.insert(30)
    test_tree.insert(9)
    test_tree.insert(1)
    test_tree.insert(24)
    test_tree.insert(32)
    test_tree.insert(4)
    test_tree.insert(7)
    test_tree.printTree()


if __name__ == "__main__":
    main()
