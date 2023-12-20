from collections import deque


# self-balancing binary search tree
class AVLTree:
    def __init__(self, node, left=None, right=None):
        self.root = self
        self.node = node
        self.left = left
        self.right = right
        self.height = 1
        self.depth = 0

    def balance(self):
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0
        balanceFactor = left_height - right_height
        return abs(balanceFactor)

    def insert(self, newData):
        crr = self
        newNode = AVLTree(newData)
        newNode.height = 1
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
        # rotate the tree
        self.rotate(newNode)

    def rotate(self, newNode):
        parent = self.root
        crr = self.root
        newVal = newNode.node
        while crr is not newNode:
            if crr.balance() > 1:
                left_balance = crr.left.balance() if crr.left is not None else 0
                right_balance = crr.right.balance() if crr.right is not None else 0
                if left_balance > right_balance:
                    if crr is self.root:
                        crr = crr.left
                        self.root = crr
                        parent.left = None
                        crr.right = parent

                        crr.height = parent.height
                        crr_left = crr.left
                        while crr_left:
                            crr_left.depth -= 1
                            crr_left = crr_left.left
                        parent.depth += 1
                        parent.height -= 1
                        break
            if crr.node > newVal:
                crr = crr.left
            else:
                crr = crr.right

    def recalculateDepth(self, new_depth):
        self.depth = new_depth
        if self.left is not None:
            self.left.recalculateDepth(new_depth+1)
        if self.right is not None:
            self.right.recalculateDepth(new_depth+1)

    def rotateLeftLeft(self, parent):
        pass

    def rotateRightRight(self):
        pass

    def rotateLeftRight(self):
        pass

    def rotateRightLeft(self):
        pass

    def re_calculate_height(self, newNode):
        crr = self.root
        root_height = 1
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
                branch_list[next_depth - 1].append('/')
            else:
                temp_list[next_depth].append('')
                branch_list[next_depth - 1].append('')

            if crr.right is not None:
                queue.append(crr.right)
                temp_list[next_depth].append(str(crr.right.node))
                branch_list[next_depth - 1].append('\\')
            else:
                temp_list[next_depth].append('')
                branch_list[next_depth - 1].append('')
            done.append(crr)

        for i in range(len(temp_list)):
            n = tree_height - i
            m = tree_height - i
            # print('*'*n, '   '.join(temp_list[i]))
            print(' ' * n, end='  ')
            for j in range(len(temp_list[i])):
                print(temp_list[i][j], end='  ' if temp_list[i][j] != '' else '')
            print()
            print(' ' * m, ' '.join(branch_list[i]))

    def delete(self):
        pass

    def search(self):
        pass


def main():
    '''test_tree = AVLTree(10)
    test_tree.insert(4)
    test_tree.insert(5)
    test_tree.insert(11)
    test_tree.insert(30)
    test_tree.insert(9)
    test_tree.insert(1)
    test_tree.insert(0)
    test_tree.insert(24)
    test_tree.insert(32)
    test_tree.insert(3)
    test_tree.insert(2)
    test_tree.insert(7)
    test_tree.printTree()'''
    #       10
    #      / \
    #      4  11
    #     / \  \
    #     1  5  30
    #    / \  \ / \
    #    0  3  9  24  32
    #     /  /
    #   2  7

    test_tree2 = AVLTree(9)
    test_tree2.insert(4)
    test_tree2.insert(1)
    '''test_tree2.insert(5)
    test_tree2.insert(11)
    test_tree2.insert(10)
    test_tree2.insert(14)
    test_tree2.insert(15)
    test_tree2.insert(20)'''
    test_tree2.root.printTree()
    print(test_tree2.root.node)
    #       9
    #      / \
    #      4  14
    #     / \
    #     1  5
    #    / \
    #    11  15
    #    \
    #   20


if __name__ == "__main__":
    main()
