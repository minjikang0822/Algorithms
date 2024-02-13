import heapq


def min_heapsort(iterable):
    h = []
    result = []
    # insert value to h
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


def max_heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


arr = [4, 3, 5, 7, 1, 2, 0]

res1 = min_heapsort(arr)
res2 = max_heapsort(arr)

print("----- min heap -----")
print(" ".join(map(str, res1)))

print("----- max heap -----")
print(" ".join(map(str, res2)))
