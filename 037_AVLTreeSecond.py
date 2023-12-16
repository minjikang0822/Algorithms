from collections import deque


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1
        self.depth = 1

    def balance(self):
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0
        return abs(left_height - right_height)


class AVLTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, newVal):
        newNode = Node(newVal)
        crr = self.root
        crr_parent = crr
        while True:
            if crr.key > newVal:
                crr.height += 1
                if crr.left is None:
                    newNode.depth = crr.depth + 1
                    crr.left = newNode
                    if crr.right is not None:
                        self.resetHeight(newNode)
                    self.updateRootHeight()
                    break
                crr_parent = crr
                crr = crr.left
            else:
                crr.height += 1
                if crr.right is None:
                    newNode.depth = crr.depth + 1
                    crr.right = newNode
                    if crr.left is not None:
                        self.resetHeight(newNode)
                    self.updateRootHeight()
                    if crr_parent.balance() > 1:
                        self.leftRotation(crr_parent)
                    break
                crr_parent = crr
                crr = crr.right

    def updateRootHeight(self):
        left_height = self.root.left.height if self.root.left is not None else 0
        right_height = self.root.right.height if self.root.right is not None else 0
        self.root.height = max(left_height, right_height) + 1

    def resetHeight(self, newNode):
        crr = self.root
        newVal = newNode.key
        while crr is not newNode:
            crr.height -= 1
            if crr.key > newVal:
                crr = crr.left
            else:
                crr = crr.right

    """
    LEFT ROTATION
              A                       R
           /     \                /       \
          L       R     ==>      A        RR
                /   \          /   \
               RL   RR        L     RL
    """

    def leftRotation(self, A):
        print("Left Rotate at", A.key)
        A_parent = self.root
        target_value = A.key
        if A is not self.root:
            while A_parent.left is A or A_parent.right is A:
                if A_parent.key > target_value:
                    A_parent = A_parent.left
                else:
                    A_parent = A_parent.right

        R = A.right
        RL = R.left

        A.right = RL
        R.left = A
        if A is self.root:
            R.depth = 1
            self.root = R
            A_parent = self.root
        else:
            if A_parent.left is A:
                A_parent.left = R
            else:
                A_parent.right = R
        L = A.left
        A.height = max(L.height if L is not None else 0, RL.height if RL is not None else 0) + 1
        R.height = max(A.height, R.right.height) + 1
        self.recalculateDepth(A_parent)

    def recalculateDepth(self, parent):
        parent_depth = parent.depth
        if parent.left is not None:
            parent.left.depth = parent_depth + 1
            self.recalculateDepth(parent.left)
        if parent.right is not None:
            parent.right.depth = parent_depth + 1
            self.recalculateDepth(parent.right)

    """
    RIGHT ROTATION
              A                       L
           /     \                /       \
          L       R     ==>      LL         A
        /   \                             /   \          
       LL   LR                           LR    R
    """

    def printTree(self):
        tree_height = self.root.height
        temp_list = [[] for _ in range(tree_height + 1)]
        branch_list = [[] for _ in range(tree_height + 1)]
        temp_list[0] = [str(self.root.key)]
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
                temp_list[next_depth].append(str(crr.left.key))
                branch_list[next_depth - 1].append('/')
            else:
                temp_list[next_depth].append('')
                branch_list[next_depth - 1].append('')

            if crr.right is not None:
                queue.append(crr.right)
                temp_list[next_depth].append(str(crr.right.key))
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

    test_tree2 = AVLTree(3)
    test_tree2.insert(4)
    test_tree2.insert(5)
    # test_tree2.printTree()
    print(test_tree2.root.depth)
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
