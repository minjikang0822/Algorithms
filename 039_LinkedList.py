class SinglyLinkedList:
    def __init__(self, node, nextNode=None):
        self.node = node
        self.nextNode = nextNode

    def insertion(self, newNode, next_to=None):
        crr = self
        # insert at the end of the list
        if next_to is None:
            while crr.nextNode is not None:
                crr = crr.nextNode
            crr.nextNode = SinglyLinkedList(newNode)
        else:
            while crr.node != next_to:
                crr = crr.nextNode
            tempNode = crr.nextNode
            newNext = SinglyLinkedList(newNode, tempNode)
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

    def printLinkedList(self):
        crr = self
        while crr.nextNode is not None:
            print(crr.node, end=" -> ")
            crr = crr.nextNode
        print(crr.node)


class DoublyLinkedList:
    def __init__(self, node, nextNode, previousNode):
        self.node = node
        self.nextNode = nextNode
        self.previousNode = previousNode

    def insertBefore(self):
        pass

    def insertAfter(self):
        pass




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
    linkedlist1 = SinglyLinkedList(1)
    linkedlist1.insertion(2)
    linkedlist1.insertion(3)
    linkedlist1.insertion(4)
    linkedlist1.deletion(3)
    linkedlist1.deletion(1)
    linkedlist1.insertion(10, 2)
    linkedlist1.insertion(5)
    linkedlist1.insertion(7)
    linkedlist1.insertion(9)
    linkedlist1.printLinkedList()
    # 2 -> 10 -> 4 -> 5 -> 7 -> 9


if __name__ == "__main__":
    main()
