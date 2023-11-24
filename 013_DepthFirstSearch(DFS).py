def dfs_withRecursion(graph, start, visited=None):
    if visited is None:
        visited = [False] * len(graph)

    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs_withRecursion(graph, i, visited)


def dfs_withoutRecursion(graph, start):
    visited = [False] * len(graph)
    stack = [start]

    while stack:
        crr = stack[-1]
        if not visited[crr]:
            visited[crr] = True
            print(crr, end=" ")

        no_more = True
        for i in graph[crr]:
            if not visited[i]:
                next_node = i
                stack.append(next_node)
                visited[next_node] = True
                print(next_node, end=" ")
                no_more = False
                break
        if no_more:
            stack.pop()


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
    print("----- with    Recursion")
    dfs_withRecursion(test_graph, 1)
    print("\n----- without Recursion")
    dfs_withoutRecursion(test_graph, 1)
    # 1 2 7 6 8 3 4 5 hello


if __name__ == "__main__":
    main()
