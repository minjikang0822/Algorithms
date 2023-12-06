class Tree:
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right

    def tree_traversal(self, last, depths, nodes, depth=0):
        depths.append(depth)
        nodes.append(self.node)
        last[self.node] = len(nodes) - 1
        if self.left is not None:
            self.left.tree_traversal(last, depths, nodes, depth + 1)
            depths.append(depth)
            nodes.append(self.node)
            last[self.node] = len(nodes) - 1
        if self.right is not None:
            self.right.tree_traversal(last, depths, nodes, depth + 1)
            depths.append(depth)
            nodes.append(self.node)
            last[self.node] = len(nodes) - 1
        return last


def lca(target_tree, a, b):
    if a == b:
        return a

    last = dict()
    depths = []
    nodes = []
    last = target_tree.tree_traversal(last, depths, nodes)
    a_idx = last[a]
    b_idx = last[b]

    sliced_depths = depths[a_idx if a_idx < b_idx else b_idx: b_idx+1 if b_idx > a_idx else a_idx+1]
    lca_idx = sliced_depths.index(min(sliced_depths))
    lca_idx += a_idx if a_idx < b_idx else b_idx

    return nodes[lca_idx]


def main():
    test_tree = Tree(1, Tree(2, Tree(4, Tree(8), Tree(9)), Tree(5, Tree(10), Tree(11, Tree(14), Tree(15)))),
                     Tree(3, Tree(6), Tree(7, Tree(12), Tree(13))))

    print(lca(test_tree, 6, 5))
    print(lca(test_tree, 2, 2))
    print(lca(test_tree, 1, 2))
    print(lca(test_tree, 1, 13))
    print(lca(test_tree, 4, 14))


if __name__ == "__main__":
    main()
