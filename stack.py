class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, item):
        self.stack.append(item)
        print(item, ' inserted')
        self.printStack()

    def printStack(self):
        print('Current Stack: |' + '|'.join(map(str, self.stack)) + '|')

    def pop(self):
        # Last In First Out (LIFO)
        # pop() remove and return the item at the last index
        removed_item = self.stack.pop()
        print(removed_item, ' removed')
        self.printStack()
        return removed_item

    def reverse(self):
        # [::-1] reverse the list
        self.stack = self.stack[::-1]
        print("reversed")
        self.printStack()


def main():
    stack1 = Stack()

    # |1|
    stack1.insert(1)

    # |1|2|
    stack1.insert(2)

    # |1|2|3|
    stack1.insert(3)

    # |1|2|
    stack1.pop()

    # |1|2|4|
    stack1.insert(4)

    # |4|2|1|
    stack1.reverse()


if __name__ == "__main__":
    main()
