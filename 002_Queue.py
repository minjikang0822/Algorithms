from collections import deque


class Queue():
    def __init__(self):
        self.queue = deque()

    def printQueue(self):
        print("Current Queue: |" + '|'.join(map(str, self.queue)) + '|')

    def insert(self, item):
        self.queue.append(item)
        print(item, 'inserted')
        self.printQueue()

    def pop(self):
        # First in First Out
        # remove the very left one from the queue which was inserted very earlier
        removed_item = self.queue.popleft()
        print(removed_item, 'removed')
        self.printQueue()

    def reverse(self):
        self.queue.reverse()
        print("reversed")
        self.printQueue()


def main():
    queue1 = Queue()

    # |1|
    queue1.insert(1)

    # |1|2|
    queue1.insert(2)

    # |1|2|3|
    queue1.insert(3)

    # |2|3|
    queue1.pop()

    # |2|3|4|
    queue1.insert(4)

    # |4|3|2|
    queue1.reverse()


if __name__ == "__main__":
    main()
