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
            crr.height += 1
            if crr.key > newVal:
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
                if crr.right is None:
                    newNode.depth = crr.depth + 1
                    crr.right = newNode
                    if crr.left is not None:
                        self.resetHeight(newNode)
                    self.updateRootHeight()
                    print("crr: ", crr.key)
                    if self.root.balance() > 1:
                        self.leftRotation(self.unbalanced_A(crr))
                    break
                crr_parent = crr
                crr = crr.right

    def unbalanced_A(self, target):
        target_key = target.key
        crr = self.root
        A = crr
        while crr is not target:
            if crr.balance() > 1:
                A = crr
            if crr.key > target_key:
                crr = crr.left
            else:
                crr = crr.right
        return A

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

        R = A.right
        RL = R.left

        A.right = RL
        R.left = A
        L = A.left

        if A is not self.root:
            while True:
                if A_parent.key > target_value:
                    if A_parent.left is A:
                        A_parent.left = R
                        R.depth -= 1
                        break
                    A_parent = A_parent.left
                else:
                    if A_parent.right is A:
                        A_parent.right = R
                        R.depth -= 1
                        break
                    A_parent = A_parent.right
        else:
            R.depth = 1
            self.root = R
            A_parent = self.root
        print("parent", A_parent.key)

        A.height = max(L.height if L is not None else 0, RL.height if RL is not None else 0) + 1
        R.height = max(A.height, R.right.height) + 1

        self.recalculateDepth(R)

    def recalculateDepth(self, R):
        parent_depth = R.depth
        if R.left is not None:
            R.left.depth = parent_depth + 1
            self.recalculateDepth(R.left)
        if R.right is not None:
            R.right.depth = parent_depth + 1
            self.recalculateDepth(R.right)

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
        node_list = [[] for _ in range(tree_height + 1)]
        branch_list = [[] for _ in range(tree_height + 2)]
        node_list[1] = [str(self.root.key)]
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
                node_list[next_depth].append(str(crr.left.key))
                branch_list[next_depth].append('/')
            else:
                node_list[next_depth].append('')
                branch_list[next_depth].append('')

            if crr.right is not None:
                queue.append(crr.right)
                node_list[next_depth].append(str(crr.right.key))
                branch_list[next_depth].append('\\')
            else:
                node_list[next_depth].append('')
                branch_list[next_depth].append('')
            done.append(crr)
        node_list = node_list[1:]
        branch_list = branch_list[1:]
        for i in range(len(node_list)):
            n = tree_height - i
            for j in range(len(node_list[i])):
                print(node_list[i][j], end='  ' if node_list[i][j] != '' else '')
            print("\n", ' '.join(branch_list[i+1]))


def main():
    test_tree = AVLTree(3)
    test_tree.insert(4)
    test_tree.insert(5)
    test_tree.insert(7)
    test_tree.insert(9)
    test_tree.insert(10)
    test_tree.printTree()
#    test_node = test_tree.root.right.right.right
#    print(test_node.key)
#    print(test_node.height)
#    print(test_tree.root.balance())


if __name__ == "__main__":
    main()
