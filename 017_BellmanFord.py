def bellmanFord(node_info, start):
    n = len(node_info.keys())
    INF = 10**8
    dist_node = [INF for _ in range(n+1)]
    dist_node[start] = 0
    neg_cycle = False
    for i in range(n):
        for node in node_info:
            crr_dist = dist_node[node]
            for connected in node_info[node]:
                connected_node = connected[0]
                connected_dist = connected[1]
                temp_dist = crr_dist + connected_dist
                old_dist = dist_node[connected_node]

                if temp_dist < old_dist:
                    dist_node[connected_node] = temp_dist
                    if i == n-1:
                        neg_cycle = True
                        dist_node[connected_node] = -1 * INF
    # idx 0 is just a padding
    print(dist_node[1:])
    if neg_cycle:
        print("There is a negative cycle")
    else:
        print("There is NOT negative cycle")
    return neg_cycle, dist_node


def main():
    node_info = {
        1: [[2, 6], [3, 2]],
        2: [[3, 2], [4, 2]],
        3: [[5, 1]],
        4: [[6, 2]],
        5: [[4, 3], [6, 4], [2, -2]],
        6: []
    }
    start = 1
    end = 3
    neg_cycle,  dist_node = bellmanFord(node_info, start)
    print(f"Minimum dist from node {start} to node {end} is", "NOT AVAILABLE" if neg_cycle else dist_node[3])
    # [0, 1, 2, 3, 3, 5]
    # There is NOT negative cycle
    # Minimum dist from node 1 to node 3 is 2

    print("--------------------")

    node_info2 = {
        1: [[2, 6], [3, 2]],
        2: [[3, 2], [4, 2]],
        3: [[5, 1]],
        4: [[6, 2]],
        5: [[4, 3], [6, 4], [2, -4]],
        6: []
    }
    start2 = 1
    end2 = 3
    neg_cycle2, dist_node2 = bellmanFord(node_info2, start2)
    print(f"Minimum dist from node {start2} to node {end2} is", "NOT AVAILABLE" if neg_cycle2 else dist_node2[3])
    # [0, -100000000, -100000000, -100000000, -100000000, -100000000]
    # There is a negative cycle
    # Minimum dist from node 1 to node 3 is NOT AVAILABLE


if __name__ == "__main__":
    main()
