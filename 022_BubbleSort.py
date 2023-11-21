def bubbleSort(target, is_descending=False):
    for i in range(len(target)-1, 0, -1):
        for j in range(0, i, 1):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
    if is_descending:
        target = target[::-1]
    return target


def main():
    test = [3, 546, 55, 1, -67, -1, -20, -50, 32, 70, 99, 201, 4305, -45]
    print("Ascending Sorting -----")
    print(bubbleSort(test))
    # [-67, -50, -45, -20, -1, 1, 3, 32, 55, 70, 99, 201, 546, 4305]
    print("Descending Sorting -----")
    print(bubbleSort(test, True))
    # [4305, 546, 201, 99, 70, 55, 32, 3, 1, -1, -20, -45, -50, -67]


if __name__ == "__main__":
    main()