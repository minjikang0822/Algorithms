import heapq


def min_heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
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
for item in res1:
    print(item)

print("----- max heap -----")
for item in res2:
    print(item)
