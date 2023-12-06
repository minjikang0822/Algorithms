from collections import deque


def topologicalSort(n, graph):
    indegree = [0 for _ in range(n+1)]
    indegree[0] = 10**8
    queue = deque()
    for edge in graph:
        indegree[edge[1]] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        crr = queue.popleft()
        print(crr, end=' ')
        for edge in graph:
            if edge[0] == crr:
                target = edge[1]
                indegree[target] -= 1
                if indegree[target] == 0:
                    queue.append(target)


def main():
    test_graph = [
        [1, 2],
        [1, 5],
        [2, 3],
        [2, 6],
        [3, 4],
        [4, 7],
        [5, 6],
        [6, 4]
    ]
    n = 7
    topologicalSort(n, test_graph)
    # 1 2 5 3 6 4 7


if __name__ == "__main__":
    main()
