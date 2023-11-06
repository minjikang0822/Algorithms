class maxHeap:
    def __init__(self, arr=None):
        if arr is None:
            self.heap = []
        else:
            self.heapify(arr)

    def heapify(self, arr):
        for item in arr:
            self.insert(item)

    def parentIndex(self, crrIdx):
        return (crrIdx - 1) // 2 if crrIdx > 0 else 0

    def leftChildIndex(self, crrIdx):
        left_idx = (crrIdx * 2) + 1
        return left_idx

    def rightChildIndex(self, crrIdx):
        right_idx = (crrIdx * 2) + 2
        return right_idx

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
            end = end + (2**from_top)
        print("--------------------------")


def main():
    maxheap = maxHeap()
    maxheap.insert(1)
    maxheap.insert(2)
    maxheap.insert(3)
    maxheap.insert(4)
    maxheap.insert(9)
    maxheap.insert(7)
    maxheap.insert(8)
    maxheap.insert(0)
    maxheap.insert(5)
    maxheap.insert(6)

    maxheap.insert(7)
    maxheap.insert(8)
    maxheap.insert(0)
    maxheap.insert(5)
    maxheap.insert(6)
    maxheap.insert(7)
    maxheap.insert(8)
    maxheap.insert(0)
    maxheap.insert(5)
    maxheap.delete(7)


if __name__ == "__main__":
    main()
