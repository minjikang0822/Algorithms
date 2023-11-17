def insertionSort_A(target):
    for i in range(1, len(target), 1):
        for j in range(i, 0, -1):
            if target[j] < target[j - 1]:
                target[j], target[j - 1] = target[j - 1], target[j]
            else:
                break


def insertionSort_D(target):
    for i in range(1, len(target), 1):
        for j in range(i, 0, -1):
            if target[j] > target[j - 1]:
                target[j], target[j - 1] = target[j - 1], target[j]
            else:
                break


def main():
    init = [9, 2, 1, 5, 4, 0, 3, 8, 7, 6]

    print("Ascending Sorting -----")
    insertionSort_A(init)
    print(init)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Descending Sorting -----")
    insertionSort_D(init)
    print(init)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


if __name__ == "__main__":
    main()
