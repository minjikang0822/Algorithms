class node:
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
        self.root = root

    """
    LEFT ROTATION
              A                       R
           /     \                /       \
          L       R     ==>      A        RR
                /   \          /   \
               RL   RR        L     RL
    """

    def leftRotation(self, A):
        A_parent = self.root
        target_value = A.key
        while A_parent.left is A or A_parent.right is A:
            if A_parent.key > target_value:
                A_parent = A_parent.left
            else:
                A_parent = A_parent.right
        R = A.right
        RL = R.left

        A.right = RL
        R.left = A

        if A_parent.left is A:
            A_parent.left = R
        else:
            A_parent.right = R

    """
    RIGHT ROTATION
              A                       L
           /     \                /       \
          L       R     ==>      LL         A
        /   \                             /   \          
       LL   LR                           LR    R
    """


