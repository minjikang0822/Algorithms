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
        self.recalculateHeight(newNode)
        self.printTree()
        A, A_parent = self.unbalanced_A(crr)

        # LEFT HEAVY => Right Rotation OR Left-Right Rotation
        if A.balance() > 1:
            L = A.left
            subLeft_height = L.left.height if L.left is not None else -1
            subRight_height = L.right.height if L.right is not None else -1

            # CASE #1: RIGHT ROTATION
            # ***LEFT HEAVY*** + NEW NODE INSERTED TO LL
            if subLeft_height > subRight_height:
                self.rightRotation(A, A_parent)

            # CASE #2: LEFT RIGHT ROTATION
            # ***LEFT HEAVY*** + NEW NODE INSERTED TO LR
            else:
                # CASE #2-A: NEW NODE added as a LEFT CHILD of LR
                if crr.right is None:
                    self.leftRightRotation_A(A, A_parent)

                # CASE #2-B: NEW NODE added as a RIGHT CHILD of LR
                else:
                    self.leftRightRotation_B(A, A_parent)

        # RIGHT HEAVY => Left Rotation OR Right-Left Rotation
        elif A.balance() < -1:
            R = A.right
            subLeft_height = R.left.height if R.left is not None else -1
            subRight_height = R.right.height if R.right is not None else -1

            # CASE #3: LEFT ROTATION
            # ***RIGHT HEAVY*** + NEW NODE INSERTED TO RR
            if subLeft_height < subRight_height:
                self.leftRotation(A, A_parent)

            # CASE #4: RIGHT LEFT ROTATION
            # ***RIGHT HEAVY*** + NEW NODE INSERTED TO LR
            else:
                # CASE #4-A: NEW NODE added as a LEFT CHILD of RL
                if crr.right is None:
                    self.rightLeftRotation_A(A, A_parent)

                # CASE #4-B: NEW NODE added as a RIGHT CHILD of RL
                else:
                    self.rightLeftRotation_B(A, A_parent)

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
        L = A.left
        LL = L.left
        LR = L.right
        R = A.right

        L.right = A
        A.left = LR

        if A is self.root:
            L.depth = 0
            A_parent = L
            self.root = L
        else:
            if A_parent.balance() > 1:
                A_parent.left = L
            else:
                A_parent.right = L

        A.height = max(LR.height if LR is not None else -1, R.height if R is not None else -1) + 1
        L.height = max(LL.height if LL is not None else -1, A.height if A is not None else -1) + 1

        self.recalculateHeight(L)
        self.recalculateDepth(A_parent)

        print("----- Right Rotation at", A.key, "-----")
        self.printTree()

    def leftRightRotation_A(self, A, A_parent):
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
        """

        L = A.left
        R = A.right
        LL = L.left
        LR = L.right
        NEW_NODE = LR.left

        # STEP01: LEFT ROTATION
        L.right = NEW_NODE
        LR.left = L
        A.left = LR

        # STEP02: RIGHT ROTATION
        A.left = None
        LR.right = A

        if A is self.root:
            LR.depth = 0
            A_parent = LR
            self.root = LR
        else:
            if A_parent.balance() > 1:
                A_parent.left = LR
            else:
                A_parent.right = LR

        L.height = max(LL.height if LL is not None else -1, NEW_NODE.height) + 1
        A.height = (R.height if R is not None else -1) + 1
        LR.height = max(L.height if L is not None else -1, A.height if A is not None else -1) + 1

        self.recalculateHeight(LR)
        self.recalculateDepth(A_parent)

        print("Left Right Rotate (A) at", A.key)
        self.printTree()

    def leftRightRotation_B(self, A, A_parent):
        """
            CASE #2: LEFT RIGHT ROTATION
            B)
                      A                        A                         LR
                   /     \      LEFT       /       \      RIGHT      /        \
                  L       R     ==>      LR         R      ==>      L          A
                /   \                  /  \                        /        /     \
               LL   LR               L   *NEW NODE*               LL   *NEW NODE*  R
                      \             /
                  *NEW NODE*      LL
        """

        L = A.left
        R = A.right
        LL = L.left
        LR = L.right
        NEW_NODE = LR.right

        # STEP01: LEFT ROTATION
        L.right = None
        LR.left = L
        A.left = LR

        # STEP02: RIGHT ROTATION
        A.left = NEW_NODE
        LR.right = A

        if A is self.root:
            LR.depth = 0
            A_parent = LR
            self.root = LR
        else:
            if A_parent.balance() > 1:
                A_parent.left = LR
            else:
                A_parent.right = LR

        L.height = (LL.height if LL is not None else -1) + 1
        A.height = max(R.height if R is not None else -1, NEW_NODE.height) + 1
        LR.height = max(L.height if L is not None else -1, A.height if A is not None else -1) + 1

        self.recalculateHeight(LR)
        self.recalculateDepth(A_parent)

        print("Left Right Rotate (B) at", A.key)
        self.printTree()

    def leftRotation(self, A, A_parent):
        """
            CASE #3: LEFT ROTATION
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
            if A_parent.balance() > 1:
                A_parent.left = R
            else:
                A_parent.right = R

        A.height = max(L.height if L is not None else -1, RL.height if RL is not None else -1) + 1
        R.height = max(A.height if A is not None else -1, RR.height if RR is not None else -1) + 1
        self.recalculateHeight(R)
        self.recalculateDepth(A_parent)
        print("----- Left Rotation at", A.key, "-----")
        self.printTree()

    def rightLeftRotation_A(self, A, A_parent):
        """
            CASE #4: RIGHT LEFT ROTATION
            A)
                      A                        A                         RL
                   /     \      RIGHT      /       \       LEFT      /        \
                  L       R      ==>      L        RL      ==>      A          R
                        /   \                   /      \          /   \         \
                       RL   RR            *NEW NODE*    R        L  *NEW NODE*  RR
                      /                                  \
                     *NEW NODE*                          RR
        """

        L = A.left
        R = A.right
        RL = R.left
        RR = R.right
        NEW_NODE = RL.left

        # STEP01: RIGHT ROTATION
        R.left = None
        RL.right = R
        A.right = RL

        # STEP02: LEFT ROTATION
        A.right = NEW_NODE
        RL.left = A

        if A is self.root:
            RL.depth = 0
            A_parent = RL
            self.root = RL
        else:
            if A_parent.balance() > 1:
                A_parent.left = RL
            else:
                A_parent.right = RL

        A.height = max(L.height if L is not None else -1, NEW_NODE.height) + 1
        R.height = (RR.height if RR is not None else -1) + 1
        RL.height = max(A.height if A is not None else -1, R.height if R is not None else -1) + 1

        self.recalculateHeight(RL)
        self.recalculateDepth(A_parent)

        print("----- Right Left Rotation (A) at", A.key, "-----")
        self.printTree()

    def rightLeftRotation_B(self, A, A_parent):
        """
            CASE #4: RIGHT LEFT ROTATION
            B)
                      A                        A                         RL
                   /     \      RIGHT      /       \       LEFT      /        \
                  L       R      ==>      L        RL      ==>      A          R
                        /   \                       \              /        /      \
                       RL   RR                       R            L    *NEW NODE*   RR
                        \                        /       \
                    *NEW NODE*              *NEW NODE*   RR
        """

        L = A.left
        R = A.right
        RL = R.left
        RR = R.right
        NEW_NODE = RL.right

        # STEP01: RIGHT ROTATION
        R.left = NEW_NODE
        RL.left = None
        RL.right = R
        A.right = RL

        # STEP02: LEFT ROTATION
        A.right = None
        RL.left = A

        if A is self.root:
            RL.depth = 0
            A_parent = RL
            self.root = RL
        else:
            if A_parent.balance() > 1:
                A_parent.left = RL
            else:
                A_parent.right = RL

        A.height = (L.height if L is not None else -1) + 1
        R.height = max(RR.height if RR is not None else -1, NEW_NODE.height) + 1
        RL.height = max(A.height if A is not None else -1, R.height if R is not None else -1) + 1

        self.recalculateHeight(RL)
        self.recalculateDepth(A_parent)

        print("----- Right Left Rotation (B) at", A.key, "-----")
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
            print("subRootKey", subRootKey)
            print("crr.key", crr.key)
            if crr.key > subRootKey:
                crr = crr.left
            else:
                crr = crr.right

        leftHeight = subRootParent.left.height if subRootParent.left is not None else -1
        rightHeight = subRootParent.right.height if subRootParent.right is not None else -1
        subRootParent.height = max(leftHeight, rightHeight) + 1
        self.recalculateHeight(subRootParent)

    def search(self, target):
        crr = self.root
        crr_parent = self.root
        while crr.key != target:
            crr_parent = crr
            if crr.key > target:
                crr = crr.left
            else:
                crr = crr.right

            if crr is None:
                print(target, "does NOT exist in the AVL Tree")
                return None, None
        print(target, "found")
        return crr, crr_parent

    def delete(self, target):
        to_delete, toDelete_parent = self.search(target)
        successor, successor_parent = self.findInOrderSuccessor(to_delete)
        print("test01", successor_parent.key)
        if to_delete is None:
            print("Since", target, "does not exist, it CANNOT be deleted")
            return
        elif to_delete is self.root:
            # there is no node than just root node
            if successor is None:
                self.root = None
                return
            else:
                if successor_parent.left is successor:
                    successor_parent.left = None
                elif successor_parent.right is successor:
                    successor_parent.right = None
                self.root.key = successor.key
        else:
            print("test02", successor_parent.key)
            if successor_parent.left is successor:
                successor_parent.left = None
            elif successor_parent.right is successor:
                successor_parent.right = None
            print("test02.5", successor_parent)
            # CASE 1: The node to delete does not have any child
            if successor.left is None and successor.right is None:
                if toDelete_parent.left is to_delete:
                    toDelete_parent.left.key = successor
                else:
                    toDelete_parent.right.key = successor
                print("test03", successor_parent.key)
            # CASE 2: The node to delete has both left and right child
            elif successor.left is not None and successor.right is not None:
                # to do
                pass
            # CASE 3: The node to delete has only left child
            elif successor.left is not None:
                pass
            # CASE 4: The node to delete has only right child
            else:
                pass
        print("test04", successor_parent.key)
        successor_parent.height = max(successor_parent.left.height if successor_parent.left is not None else -1,
                                      successor_parent.right.height if successor_parent.right is not None else -1) + 1
        print("parent", successor_parent.key)
        self.recalculateHeight(successor_parent)
        self.recalculateDepth(self.root)
        print(target, "DELETED")
        self.printTree()

    def findInOrderSuccessor(self, target):
        to_delete, to_delete_parent = self.search(target)
        parent = target
        crr = target.left
        if crr is not None:
            while crr.right is not None:
                parent = crr
                crr = crr.right
        else:
            crr = target.right
            if crr is not None:
                while crr.left is not None:
                    parent = crr
                    crr = crr.left
        return crr, parent

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
                continue
            print("\n", ' '.join(branch_list[i]))
        print("\n------------------------------")


def main():
    """
    print("EX1) EXAMPLE FOR RIGHT ROTATION")
    ex01 = AVLTree(30)
    new_nodes01 = [10, 40, 5, 20, 35, 45, 3, 7, 15, 25, 30, 37, 42, 47, 2, 4, 6, 8, 1]
    for node in new_nodes01:
        ex01.insert(node)
    """

    """
    print("EX2) EXAMPLE FOR LEFT RIGHT ROTATION")
    ex02 = AVLTree(50)
    new_nodes02 = [20, 80, 10, 40, 30, 45, 5, 15, 17]
    for node in new_nodes02:
        ex02.insert(node)
    """

    """
        print("EX3) EXAMPLE FOR LEFT ROTATION")
        ex03 = AVLTree(3)
        new_nodes03 = [4, 5, 8, 9, 10, 11, 6, 7]
        for node in new_nodes03:
            ex03.insert(node)
        '''
                        8
                    /        \
                   4         10
                 /   \      /   \
                3     6    9    11
                    /   \
                    5    7
        '''
    """

    print("EX4) EXAMPLE FOR RIGHT LEFT ROTATION")
    ex04 = AVLTree(50)
    new_nodes04 = [20, 80, 60, 100, 55, 70, 90, 120, 95]
    for node in new_nodes04:
        ex04.insert(node)
    '''
             60  
          /      \ 
         50      90  
        / \      / \ 
       20  55  80  100  
              /    / \ 
             70  95  120
    '''
    ex04.search(1)
    ex04.search(20)
    ex04.delete(60)
    ex04.delete(100)
    ex04.delete(90)
    ex04.search(60)

    test_node = ex04.root
    test_node.printNodeInfo()


if __name__ == "__main__":
    main()
