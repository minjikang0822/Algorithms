from collections import deque


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 0
        self.depth = 0

    def balance(self):
        left_height = self.left.height if self.left is not None else -1
        right_height = self.right.height if self.right is not None else -1
        return left_height - right_height

    def printNodeInfo(self):
        print("key:", self.key, end=" | ")
        print("height:", self.height, end=" | ")
        print("depth:", self.depth, end=" | ")
        print("balance:", self.balance())


class AVLTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, newVal):
        newNode = Node(newVal)
        crr = self.root
        while True:
            if crr.key > newVal:
                if crr.left is None:
                    newNode.depth = crr.depth + 1
                    crr.left = newNode
                    break
                crr = crr.left
            # crr.key <= newVal
            else:
                if crr.right is None:
                    newNode.depth = crr.depth + 1
                    crr.right = newNode
                    break
                crr = crr.right
        print("---------", newVal, "inserted ---------")
        self.printTree()
        self.recalculateHeight(newNode)
        A, A_parent = self.unbalanced_A(crr)
        # RIGHT HEAVY => Left Rotation OR Right-Left Rotation
        if A.balance() < -1:
            L = A.left
            R = A.right
            subLeft_height = R.left.height if R.left is not None else -1
            subRight_height = R.right.height if R.right is not None else -1
            # CASE #1: LEFT ROTATION
            # ***RIGHT HEAVY*** + NEW NODE INSERTED TO RIGHT SUBTREE
            if subLeft_height < subRight_height:
                self.leftRotation(A, A_parent)
            # ***RIGHT HEAVY*** + NEW NODE INSERTED LEFT SUBTREE HEAVY
            else:
                self.leftRightRotation(A, A_parent)

    def unbalanced_A(self, target):
        target_key = target.key
        crr = self.root
        crr_parent = self.root
        A = crr
        A_parent = crr_parent
        while crr is not target:
            if abs(crr.balance()) > 1:
                A = crr
                A_parent = crr_parent
            if crr.key > target_key:
                crr_parent = crr
                crr = crr.left
            else:
                crr_parent = crr
                crr = crr.right
        return A, A_parent

    def leftRotation(self, A, A_parent):
        """
            CASE #4: LEFT ROTATION
                      A                       R
                   /     \                /       \
                  L       R     ==>      A        RR
                        /   \          /   \       |
                       RL   RR        L     RL   *NEW NODE*
                            |
                        *NEW NODE*
        """

        L = A.left
        R = A.right
        RL = R.left
        RR = R.right

        A.right = RL
        R.left = A

        if A is self.root:
            R.depth = 0
            A_parent = R
            self.root = A_parent
        else:
            A_parent.right = R

        A.height = max(L.height if L is not None else -1, RL.height if RL is not None else -1) + 1
        R.height = max(A.height if A is not None else -1, RR.height if RR is not None else -1) + 1
        self.recalculateHeight(R)
        self.recalculateDepth(A_parent)
        print("----- Left Rotation at", A.key, "-----")
        self.printTree()

    def rightRotation(self, A, A_parent):
        """
            CASE #1: RIGHT ROTATION
                      A                       L
                   /     \                /       \
                  L       R     ==>      LL         A
                /   \                    |        /   \
               LL   LR              *NEW NODE*   LR    R
               |
           *NEW NODE*
        """
        print("----- Right Rotation at", A.key, "-----")
        self.printTree()

    def leftRightRotation(self, A, A_parent):
        """
            CASE #2: LEFT RIGHT ROTATION
            A)
                      A                        A                         LR
                   /     \      LEFT       /       \      RIGHT      /        \
                  L       R     ==>      LR         R      ==>      L          A
                /   \                   /                        /     \        \
               LL   LR                L                        LL   *NEW NODE*   R
                    /              /     \
               *NEW NODE*         LL   *NEW NODE*

            B)
                      A                        A                         LR
                   /     \      LEFT       /       \      RIGHT      /        \
                  L       R     ==>      LR         R      ==>      L          A
                /   \                  /  \                        /        /     \
               LL   LR               L   *NEW NODE*               LL   *NEW NODE*  R
                      \             /
                  *NEW NODE*      LL
        """
        print("Left Right Rotate at", A.key)
        self.printTree()

    def rightLeftRotation(self, A, A_parent):
        print("----- Right Left Rotation at", A.key, "-----")
        self.printTree()

    def recalculateDepth(self, R):
        parent_depth = R.depth
        if R.left is not None:
            R.left.depth = parent_depth + 1
            self.recalculateDepth(R.left)
        if R.right is not None:
            R.right.depth = parent_depth + 1
            self.recalculateDepth(R.right)

    def recalculateHeight(self, subRoot):
        if subRoot is self.root:
            return
        crr = self.root
        subRootParent = crr
        subRootKey = subRoot.key
        while crr is not subRoot:
            subRootParent = crr
            if crr.key > subRootKey:
                crr = crr.left
            else:
                crr = crr.right

        leftHeight = subRootParent.left.height if subRootParent.left is not None else -1
        rightHeight = subRootParent.right.height if subRootParent.right is not None else -1
        subRootParent.height = max(leftHeight, rightHeight) + 1
        self.recalculateHeight(subRootParent)

    def printTree(self):
        tree_height = self.root.height
        node_list = [[] for _ in range(tree_height + 1)]
        branch_list = [[] for _ in range(tree_height + 2)]
        node_list[0] = [str(self.root.key)]
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
                node_list[next_depth].append(' ')
                branch_list[next_depth].append('')

            if crr.right is not None:
                queue.append(crr.right)
                node_list[next_depth].append(str(crr.right.key))
                branch_list[next_depth].append('\\ ')
            else:
                node_list[next_depth].append(' ')
                branch_list[next_depth].append('')
            done.append(crr)
        branch_list = branch_list[1:]
        for i in range(len(node_list)):
            # n = tree_height - i
            for j in range(len(node_list[i])):
                print(node_list[i][j], end='  ' if node_list[i][j] != ' ' else '')
            if i == len(branch_list) - 1:
                break
            print("\n", ' '.join(branch_list[i]))
        print("\n------------------------------")


def main():
    test_tree = AVLTree(3)
    test_tree.insert(4)
    test_tree.insert(5)
    test_tree.insert(8)
    test_tree.insert(9)
    test_tree.insert(10)
    test_tree.insert(11)
    test_tree.insert(6)
    test_tree.insert(7)
    test_tree.printTree()
    '''
                    8
                /        \
               4         10
             /   \      /   \
            3     6    9    11
                /   \
                5    7
    '''
    test_node = test_tree.root.right.right
    test_node.printNodeInfo()


if __name__ == "__main__":
    main()
