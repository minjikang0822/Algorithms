class SinglyLinkedList:
    def __init__(self, node, nextNode=None):
        self.node = node
        self.nextNode = nextNode


class DoublyLinkedList:
    def __init__(self, node, nextNode, previousNode):
        self.node = node
        self.nextNode = nextNode
        self.previousNode = previousNode


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
    pass


if __name__ == "__main__":
    main()
