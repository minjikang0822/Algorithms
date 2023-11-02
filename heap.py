class maxHeap():
    def __init__(self):
        self.heap = []

    def parentIndex(self, crrIdx):
        return (crrIdx - 1) // 2 if crrIdx > 0 else 0

    def leftChildIndex(self, crrIdx):
        return (crrIdx * 2) + 1

    def rightChildIndex(self, crrIdx):
        return (crrIdx * 2) + 2

    def size(self):
        return len(self.heap)

    def height(self):
        temp = self.size()
        cnt = 0
        while temp > 1:
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
        self.printHeap()

    def printHeap(self):
        print(self.height())
        crr_depth = self.height()+1
        fromtop = 0
        while crr_depth > 0:
            start = 2**fromtop - 1
            end = start + (2**fromtop)
            print(' '*(2*crr_depth-1) + (' '*(2*crr_depth-1)).join(map(str, self.heap[start:end])))
            crr_depth -= 1
            fromtop += 1
        print("-------------")

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
    maxheap.insert(6)


if __name__ == "__main__":
    main()
