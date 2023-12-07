class LinkedList:
    def __init__(self, node, nextNode=None):
        self.node = node
        self.nextNode = nextNode

    def printLinkedList(self):
        crr = self
        while crr.nextNode is not None:
            print(crr.node, end=" -> ")
            crr = crr.nextNode
        print(crr.node)


class SinglyLinkedList(LinkedList):
    def __init__(self, node, nextNode=None):
        super().__init__(node, nextNode)

    def insertion(self, newData, next_to=None):
        crr = self
        # insert at the end of the list
        if next_to is None:
            while crr.nextNode is not None:
                crr = crr.nextNode
            crr.nextNode = SinglyLinkedList(newData)
        else:
            while crr.node != next_to:
                crr = crr.nextNode
            tempNode = crr.nextNode
            newNext = SinglyLinkedList(newData, tempNode)
            crr.nextNode = newNext

    def deletion(self, target):
        if self.node == target:
            self.node = self.nextNode.node
            self.nextNode = self.nextNode.nextNode
        else:
            prev = self
            while prev.nextNode.node != target:
                prev = prev.nextNode
            # now prev.nextNode is what we want to delete
            prev.nextNode = prev.nextNode.nextNode


class DoublyLinkedList(LinkedList):
    def __init__(self, node, previousNode=None, nextNode=None):
        super().__init__(node, nextNode)
        self.previousNode = previousNode
        self.root = self

    def insertBefore(self, newData, target=None):
        # if target is None, add the new data before its root node
        if target is None or self.root.node == target:
            crr = self.root
            while crr.previousNode is not None:
                crr = crr.previousNode
            newNode = DoublyLinkedList(newData, None, crr)
            crr.previousNode = newNode
            self.root = newNode
        else:
            after = self.root
            before = self.root
            while after.node != target:
                before = after
                after = after.nextNode
            newNode = DoublyLinkedList(newData, before, after)
            after.previousNode = newNode
            before.nextNode = newNode

    def insertAfter(self, newData, target=None):
        # if target is None, add the new data at the end of the linked list
        if target is None:
            crr = self.root
            while crr.nextNode is not None:
                crr = crr.nextNode
            newNode = DoublyLinkedList(newData, crr, None)
            crr.nextNode = newNode
        else:
            after = self.root
            afterAfter = self.root
            while after.node != target:
                after = after.nextNode
                afterAfter = after.nextNode
            newNode = DoublyLinkedList(newData, after, afterAfter)
            afterAfter.previousNode = newNode
            after.nextNode = newNode

    def delete(self, target=None):
        to_delete = self.root
        before = self.root
        # if target is None, delete the last node
        if target is None:
            while to_delete.nextNode is not None:
                before = to_delete
                to_delete = to_delete.nextNode
            before.nextNode = None
        elif target == self.root.node:
            newRoot = self.root.nextNode
            newRoot.previousNode = None
            self.root = newRoot
        else:
            after = self.root
            while to_delete.node != target:
                before = to_delete
                to_delete = to_delete.nextNode
                after = to_delete.nextNode
            before.nextNode = after
            after.previousNode = before

    def printDoublyLinkedList(self):
        self.root.printLinkedList()


class CircularSinglyLinkedList:
    def __init__(self, node, nextNode):
        self.node = node
        self.nextNode = nextNode

    def insertion(self):
        pass

    def deletion(self):
        pass


class CircularDoublyLinkedList:
    def __init__(self, node, nextNode, previousNode):
        self.node = node
        self.nextNode = nextNode
        self.previousNode = previousNode


def main():
    print("----- Singly Linked List -----")
    linkedlist1 = SinglyLinkedList(1)
    # 1
    linkedlist1.insertion(2)
    # 1 -> 2
    linkedlist1.insertion(3)
    # 1 -> 2 -> 3
    linkedlist1.insertion(4)
    # 1 -> 2 -> 3 -> 4
    linkedlist1.deletion(3)
    # 1 -> 2 -> 4
    linkedlist1.deletion(1)
    # 2 -> 4
    linkedlist1.insertion(10, 2)
    # 2 -> 10 -> 4
    linkedlist1.insertion(5)
    # 2 -> 10 -> 4 -> 5
    linkedlist1.insertion(7)
    # 2 -> 10 -> 4 -> 5 -> 7
    linkedlist1.insertion(9)
    # 2 -> 10 -> 4 -> 5 -> 7 -> 9
    linkedlist1.printLinkedList()

    print("----- Doubly Linked List -----")
    linkedList2 = DoublyLinkedList(1)
    # 1
    linkedList2.insertBefore(2)
    # 2 -> 1
    linkedList2.insertBefore(3)
    # 3 -> 2 -> 1
    linkedList2.insertBefore(4, 2)
    # 3 -> 4 -> 2 -> 1
    linkedList2.insertAfter(5, 4)
    # 3 -> 4 -> 5 -> 2 -> 1
    linkedList2.insertAfter(9)
    # 3 -> 4 -> 5 -> 2 -> 1 -> 9
    linkedList2.delete(3)
    # 4 -> 5 -> 2 -> 1 -> 9
    linkedList2.insertBefore(7)
    # 7 -> 4 -> 5 -> 2 -> 1 -> 9
    linkedList2.delete()
    # 7 -> 4 -> 5 -> 2 -> 1
    linkedList2.insertAfter(6)
    # 7 -> 4 -> 5 -> 2 -> 1 -> 6
    linkedList2.printDoublyLinkedList()


if __name__ == "__main__":
    main()
