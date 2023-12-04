def unionSet(parent_list, a, b):
    parent_a = findParent(parent_list, a)
    parent_b = findParent(parent_list, b)
    if parent_a < parent_b:
        parent_list[parent_b] = parent_a
    else:
        parent_list[parent_a] = parent_b


def findParent(parent_list, crr):
    if parent_list[crr] != crr:
        parent_list[crr] = findParent(parent_list, parent_list[crr])
    return parent_list[crr]


# DO NOT APPLY "findParent" FUNCTION BECUZ "findParent" REASSIGN EACH NODE'S PARENT TO ITS ROOT NODE
def isThereCycle(parent_list, unions):
    cycle = False
    for union in unions:
        a, b = union[0], union[1]
        if findParent(parent_list, a) == findParent(parent_list, b):
            cycle = True
            break
        else:
            unionSet(parent_list, a, b)
    print("there is a cycle" if cycle else "there is NO cycle")


def main():
    n = 6  # num of nodes
    unions = [(1, 4), (2, 3), (2, 4), (5, 6)]
    parent_list = [i for i in range(n + 1)]

    for union in unions:
        unionSet(parent_list, union[0], union[1])

    for i in range(1, n + 1, 1):
        print(i, ":", findParent(parent_list, i))


def main2():
    n2 = 6  # num of nodes
    unions2 = [(1, 4), (2, 3), (2, 4), (5, 6)]
    parent_list2 = [i for i in range(n2 + 1)]
    isThereCycle(parent_list2, unions2)
    print(parent_list2)

    n3 = 3
    unions3 = [(1, 2), (1, 3), (2, 3)]
    parent_list3 = [i for i in range(n3 + 1)]
    isThereCycle(parent_list3, unions3)
    print(parent_list3)


if __name__ == "__main__":
    main()
    main2()
