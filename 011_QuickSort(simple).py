def quickSort_A(target):
    if len(target) <= 1:
        return target
    pivot = target[0]
    left = []
    right = []
    for item in target[1:]:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)

    return quickSort_A(left) + [pivot] + quickSort_A(right)


def quickSort_D(target):
    if len(target) <= 1:
        return target

    pivot = target[0]
    left = []
    right = []
    for item in target[1:]:
        if item >= pivot:
            left.append(item)
        else:
            right.append(item)

    return quickSort_D(left) + [pivot] + quickSort_D(right)


def main():
    init = [5, 2, 1, 9, 4, 0, 3, 8, 7, 6]

    print("Ascending Sorting -----")
    print(quickSort_A(init))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Descending Sorting -----")
    print(quickSort_D(init))
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


if __name__ == "__main__":
    main()

