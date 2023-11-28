# dist_info = [[from, to, dist]]
# n = number of nodes
def floydWarshall(n, dist_info):
    graph = [[10 ** 8 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n+1, 1):
        graph[i][i] = 0

    for info in dist_info:
        from_node = info[0]
        to_node = info[1]
        dist = info[2]

        graph[from_node][to_node] = dist

    for i in range(1, n+1, 1):
        for j in range(1, n+1, 1):
            if i == j:
                continue
            for k in range(1, n+1, 1):
                if j == k:
                    continue
                temp_dist = graph[j][i] + graph[i][k]
                if graph[j][k] > temp_dist:
                    graph[j][k] = temp_dist

    for line in graph[1:]:
        print(line[1:])

    # aware that graph includes padding on line 0 and index 0 for each line
    return graph


def main():
    test = [
        [1, 2, 4],
        [1, 4, 6],
        [2, 1, 3],
        [2, 3, 7],
        [3, 1, 5],
        [3, 4, 4],
        [4, 3, 2]
    ]
    dist_graph = floydWarshall(4, test)

    # the min dist to get node #4 from node #1
    print(dist_graph[1][4])


if __name__ == "__main__":
    main()
