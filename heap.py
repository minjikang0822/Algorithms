class Heap:
    def __init__(self, arr=None):
        if arr is None:
            self.heap = []
        else:
            self.heapify(arr)

    def parentIndex(self, crrIdx):
        return (crrIdx - 1) // 2 if crrIdx > 0 else 0

    def leftChildIndex(self, crrIdx):
        left_idx = (crrIdx * 2) + 1
        return left_idx

    def rightChildIndex(self, crrIdx):
        right_idx = (crrIdx * 2) + 2
        return right_idx

    def heapify(self, arr):
        for item in arr:
            self.insert(item)

    def size(self):
        # return num of nodes in the heap
        return len(self.heap)

    def height(self):
        temp = self.size()
        cnt = 0
        while temp > 0:
            temp //= 2
            cnt += 1
        return cnt

    def printHeap(self):
        crr_depth = self.height()
        from_top = 0
        gap = 2 ** crr_depth - 1
        start = 0
        end = 1
        while crr_depth > 0:
            print(' ' * (2 ** (crr_depth - 1)) + (' ' * gap).join(map(str, self.heap[start:end])))
            gap = gap // 2
            crr_depth -= 1
            from_top += 1
            start = end
            end = end + (2 ** from_top)
        print("--------------------------")

    def insert(self, item):
        print("overwrite insert function on its child class")


class MinHeap(Heap):
    def insert(self, item):
        self.heap.append(item)
        # crrIdx is the very last index
        crrIdx = len(self.heap) - 1

        while self.heap[self.parentIndex(crrIdx)] > item:
            parentIdx = self.parentIndex(crrIdx)
            self.heap[crrIdx] = self.heap[parentIdx]
            self.heap[parentIdx] = item
            crrIdx = parentIdx
        print(f"------ '{item}' INSERTED ------")
        print(self.heap)
        self.printHeap()

    def delete(self, item):
        if item not in self.heap:
            print(f"***** {item} NOT IN THE HEAP ******")
            return
        # find the index of item to remove
        item_idx = self.heap.index(item)
        # remove the root node and place the last node at the root node
        temp_node = self.heap.pop()
        # item removed
        self.heap[item_idx] = temp_node
        # find the right place for the temp_node by swapping with smaller child
        try:
            while temp_node > self.heap[self.leftChildIndex(item_idx)] or temp_node > self.heap[self.rightChildIndex(item_idx)]:
                left_idx = self.leftChildIndex(item_idx)
                right_idx = self.rightChildIndex(item_idx)
                left_node = self.heap[left_idx]
                right_node = self.heap[right_idx]
                if left_node > right_node:
                    self.heap[right_idx] = temp_node
                    self.heap[item_idx] = right_node
                    item_idx = right_idx
                else:
                    self.heap[left_idx] = temp_node
                    self.heap[item_idx] = left_node
                    item_idx = left_idx
        # IndexError occurs when current node is a leaf node
        # in this case, there is no more node to swap
        # So stop swapping
        except IndexError:
            pass
        print(f"------ '{item}' REMOVED ------")
        print(self.heap)
        self.printHeap()


class MaxHeap(Heap):
    def insert(self, item):
        self.heap.append(item)
        # crrIdx is the very last index
        crrIdx = len(self.heap) - 1

        while self.heap[self.parentIndex(crrIdx)] < item:
            parentIdx = self.parentIndex(crrIdx)
            self.heap[crrIdx] = self.heap[parentIdx]
            self.heap[parentIdx] = item
            crrIdx = parentIdx
        print(f"------ '{item}' INSERTED ------")
        print(self.heap)
        self.printHeap()

    def delete(self, item):
        if item not in self.heap:
            print(f"***** {item} NOT IN THE HEAP ******")
            return
        # find the index of item to remove
        item_idx = self.heap.index(item)
        # remove the root node and place the last node at the root node
        temp_node = self.heap.pop()
        # item removed
        self.heap[item_idx] = temp_node
        # find the right place for the temp_node by swapping with larger child
        try:
            while temp_node < self.heap[self.leftChildIndex(item_idx)] or temp_node < self.heap[self.rightChildIndex(item_idx)]:
                left_idx = self.leftChildIndex(item_idx)
                right_idx = self.rightChildIndex(item_idx)
                left_node = self.heap[left_idx]
                right_node = self.heap[right_idx]
                if left_node < right_node:
                    self.heap[right_idx] = temp_node
                    self.heap[item_idx] = right_node
                    item_idx = right_idx
                else:
                    self.heap[left_idx] = temp_node
                    self.heap[item_idx] = left_node
                    item_idx = left_idx
        # IndexError occurs when current node is a leaf node
        # in this case, there is no more node to swap
        # So stop swapping
        except IndexError:
            pass
        print(f"------ '{item}' REMOVED ------")
        print(self.heap)
        self.printHeap()


def testMaxHeap():
    print("TEST MAX HEAP")
    max_heap = MaxHeap()
    max_heap.insert(1)
    max_heap.insert(2)
    max_heap.insert(3)
    max_heap.insert(4)

    max_heap.delete(2)

    max_heap.insert(9)
    max_heap.insert(7)
    max_heap.insert(8)

    max_heap.delete(100)
    max_heap.delete(9)

    max_heap.insert(0)
    max_heap.insert(5)
    max_heap.insert(6)

    max_heap.delete(7)
    max_heap.delete(3)


def testMinHeap():
    print("TEST MIN HEAP")
    min_heap = MinHeap()
    min_heap.insert(1)
    min_heap.insert(2)
    min_heap.insert(3)
    min_heap.insert(4)

    min_heap.delete(2)

    min_heap.insert(9)
    min_heap.insert(7)
    min_heap.insert(8)

    min_heap.delete(100)
    min_heap.delete(9)

    min_heap.insert(0)
    min_heap.insert(5)
    min_heap.insert(6)

    min_heap.delete(7)
    min_heap.delete(3)


if __name__ == "__main__":
    testMaxHeap()
    testMinHeap()
