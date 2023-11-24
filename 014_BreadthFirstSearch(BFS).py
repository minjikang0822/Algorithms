from collections import deque


def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        crr = queue.popleft()
        print(crr, end=" ")
        for node in graph[crr]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True


def main():
    test_graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    bfs(test_graph, 1)
    # 1 2 3 8 7 4 5 6


if __name__ == "__main__":
    main()
