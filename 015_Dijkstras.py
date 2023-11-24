import heapq


def dijkstra(graph, start, destination):
    INF = 10 ** 8
    dist_list = [INF] * len(graph)
    to_check = []
    heapq.heappush(to_check, (0, start))

    while to_check:
        crr = heapq.heappop(to_check)
        crr_dist = crr[0]
        crr_node = crr[1]

        if dist_list[crr_node] > crr_dist:
            dist_list[crr_node] = crr_dist
            for item in graph[crr_node]:
                heapq.heappush(to_check, (crr_dist + item[0], item[1]))
    print("Dist List: ", dist_list[1:])
    min_dist = dist_list[destination]
    return min_dist if min_dist != INF else -1


def main():
    # (dist, node)
    graph = [
        [],
        [(2, 2), (5, 3), (1, 4)],
        [(3, 3), (2, 4)],
        [(3, 2), (5, 6)],
        [(3, 3), (1, 5)],
        [(1, 3), (2, 6)],
        []
    ]

    print(dijkstra(graph, 1, 6))
    # 4


if __name__ == "__main__":
    main()
