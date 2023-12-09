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


##################################################
##################################################
##################################################


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


##################################################
##################################################
##################################################


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


##################################################
##################################################
##################################################


class CircularSinglyLinkedList(LinkedList):
    def __init__(self, node, nextNode=None):
        super().__init__(node, nextNode)
        self.head = self
        self.last = self

    def insertHead(self, newData):
        temp = self.head
        newHead = CircularSinglyLinkedList(newData, temp)
        self.head = newHead
        self.last.nextNode = newHead

    def insertLast(self, newData):
        newLast = CircularSinglyLinkedList(newData, self.head)
        self.last.nextNode = newLast
        self.last = newLast

    def insertMid(self, newData, next_to):
        crr = self.head
        while crr.node != next_to:
            crr = crr.nextNode
        newNode = CircularSinglyLinkedList(newData, crr.nextNode)
        crr.nextNode = newNode

    def deleteHead(self):
        newHead = self.head.nextNode
        self.head = newHead
        self.last.nextNode = newHead

    def deleteLast(self):
        newLast = self.head
        while newLast.nextNode is not self.last:
            newLast = newLast.nextNode
        self.last.nextNode = None
        newLast.nextNode = self.head
        self.last = newLast

    def deleteMid(self, target):
        before = self.head
        to_delete = self.head
        while to_delete.node != target:
            before = to_delete
            to_delete = to_delete.nextNode
        before.nextNode = to_delete.nextNode
        to_delete.nextNode = None

    def printCircularSinglyLinkedList(self):
        crr = self.head
        cnt = 0
        while crr != self.last:
            print(crr.node, end=' -> ')
            crr = crr.nextNode
            cnt += 1
        print(self.last.node)
        print("↑" + "_"*(4*cnt+cnt-2) + "⅃")


##################################################
##################################################
##################################################

# can make it inherited from DoublyLinkedList class
class CircularDoublyLinkedList:
    def __init__(self, node, previousNode=None, nextNode=None):
        self.node = node
        self.previousNode = previousNode
        self.nextNode = nextNode
        self.head = self
        self.last = self

    def insertHead(self, newData):
        newNode = CircularDoublyLinkedList(newData, self.last, self.head)
        self.head.previousNode = newNode
        self.last.nextNode = newNode
        self.head = newNode

    def insertLast(self, newData):
        newNode = CircularDoublyLinkedList(newData, self.last, self.head)
        self.last.nextNode = newNode
        self.head.previousNode = newNode
        self.last = newNode

    def insertMid(self, newData, next_to):
        crr = self.head
        while crr.node != next_to:
            crr = crr.nextNode
        newNode = CircularDoublyLinkedList(newData, crr, crr.nextNode)
        crr.nextNode = newNode
        crr.nextNode.previousNode = newNode

    def deleteHead(self):
        newHead = self.head.nextNode
        self.last.nextNode = newHead
        newHead.previousNode = self.last
        self.head = newHead

    def deleteLast(self):
        newLast = self.head
        while newLast.nextNode is not self.last:
            newLast = newLast.nextNode
        newLast.nextNode = self.head
        self.head.previousNode = newLast
        self.last = newLast

    def deleteMid(self, target):
        before = self.head
        to_delete = self.head
        after = self.head
        while to_delete.node != target:
            before = to_delete
            to_delete = to_delete.nextNode
            after = to_delete.nextNode
        before.nextNode = after
        after.previousNode = before

    # make its parent class
    def printCircularDoublyLinkedList(self):
        crr = self.head
        cnt = 0
        while crr is not self.last:
            print(crr.node, end=' -> ')
            crr = crr.nextNode
            cnt += 1
        print(self.last.node)
        print("↑" + "_"*(4*cnt+cnt-2) + "⅃")


def main():
    print("----- Singly Linked List -----")
    linkedList1 = SinglyLinkedList(1)
    # 1
    linkedList1.insertion(2)
    # 1 -> 2
    linkedList1.insertion(3)
    # 1 -> 2 -> 3
    linkedList1.insertion(4)
    # 1 -> 2 -> 3 -> 4
    linkedList1.deletion(3)
    # 1 -> 2 -> 4
    linkedList1.deletion(1)
    # 2 -> 4
    linkedList1.insertion(10, 2)
    # 2 -> 10 -> 4
    linkedList1.insertion(5)
    # 2 -> 10 -> 4 -> 5
    linkedList1.insertion(7)
    # 2 -> 10 -> 4 -> 5 -> 7
    linkedList1.insertion(9)
    # 2 -> 10 -> 4 -> 5 -> 7 -> 9
    linkedList1.printLinkedList()

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

    print("----- Circular Singly Linked List -----")
    linkedList3 = CircularSinglyLinkedList(1)
    linkedList3.insertHead(4)
    # 4 -> 1
    # ↑____⅃
    linkedList3.insertHead(2)
    # 2 -> 4 -> 1
    # ↑________⅃
    linkedList3.insertHead(3)
    # 3 -> 2 -> 4 -> 1
    # ↑_____________⅃
    linkedList3.insertLast(9)
    # 3 -> 2 -> 4 -> 1 -> 9
    # ↑__________________⅃
    linkedList3.insertMid(5, 4)
    # 3 -> 2 -> 4 -> 5 -> 1 -> 9
    # ↑_______________________⅃
    linkedList3.insertMid(2, 1)
    # 3 -> 2 -> 4 -> 5 -> 1 -> 2 -> 9
    # ↑____________________________⅃
    linkedList3.insertHead(9)
    # 9 -> 3 -> 2 -> 4 -> 5 -> 1 -> 2 -> 9
    # ↑_________________________________⅃
    linkedList3.deleteLast()
    # 9 -> 3 -> 2 -> 4 -> 5 -> 1 -> 2
    # ↑____________________________⅃
    linkedList3.deleteHead()
    # 3 -> 2 -> 4 -> 5 -> 1 -> 2
    # ↑_______________________⅃
    linkedList3.deleteLast()
    # 3 -> 2 -> 4 -> 5 -> 1
    # ↑__________________⅃
    linkedList3.deleteMid(4)
    # 3 -> 2 -> 5 -> 1
    # ↑_____________⅃
    linkedList3.insertMid(4, 2)
    # 3 -> 2 -> 4 -> 5 -> 1
    # ↑__________________⅃
    linkedList3.printCircularSinglyLinkedList()

    print("----- Circular Doubly Linked List -----")
    linkedList4 = CircularDoublyLinkedList(1)
    linkedList4.insertHead(3)
    # 3 -> 1
    # ↑___⅃
    linkedList4.insertHead(4)
    # 4 -> 3 -> 1
    # ↑________⅃
    linkedList4.insertLast(2)
    # 4 -> 3 -> 1 -> 2
    # ↑_____________⅃
    linkedList4.insertMid(5, 1)
    # 4 -> 3 -> 1 -> 5 -> 2
    # ↑__________________⅃
    linkedList4.insertMid(4, 3)
    # 4 -> 3 -> 4 -> 1 -> 5 -> 2
    # ↑_______________________⅃
    linkedList4.deleteLast()
    # 4 -> 3 -> 4 -> 1 -> 5
    # ↑__________________⅃
    linkedList4.deleteHead()
    # 3 -> 4 -> 1 -> 5
    # ↑_____________⅃
    linkedList4.deleteMid(1)
    # 3 -> 4 -> 5
    # ↑________⅃
    linkedList4.printCircularDoublyLinkedList()


if __name__ == "__main__":
    main()
