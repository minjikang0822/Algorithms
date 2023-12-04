module_name = "018_UnionFind"
unionFind = __import__(module_name)


def main():
    kruskalsEdges = []
    finalCost = 0
    n = 7
    # (cost, node_a, node_b)
    edges = [(29, 1, 2), (75, 1, 5), (35, 2, 3), (34, 2, 6), (7, 3, 4), (23, 4, 6), (13, 4, 7), (53, 5, 6), (25, 6, 7)]
    # would be sorted by its cost
    edges.sort()
    parent_list = [i for i in range(n+1)]
    for edge in edges:
        a, b = edge[1], edge[2]
        parent_a = unionFind.findParent(parent_list, a)
        parent_b = unionFind.findParent(parent_list, b)

        if parent_a != parent_b:
            kruskalsEdges.append(edge)
            unionFind.unionSet(parent_list, a, b)
            finalCost += edge[0]
    print(kruskalsEdges)
    # [(7, 3, 4), (13, 4, 7), (23, 4, 6), (29, 1, 2), (34, 2, 6), (53, 5, 6)]
    print(finalCost)
    # 159


if __name__ == "__main__":
    main()
