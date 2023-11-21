# Ascending
def selectionSort(target, is_ascending=True):
    for i in range(len(target)):
        min_idx = i
        for j in range(i+1, len(target), 1):
            if target[min_idx] > target[j]:
                min_idx = j
        target[i], target[min_idx] = target[min_idx], target[i]
    if not is_ascending:
        target = target[::-1]
    return target


def main():
    test = [-1, -5, 3, 60, 99, -200, 434, 52, 20, -11]
    print("Ascending Sorting -----")
    print(selectionSort(test))
    # [-200, -11, -5, -1, 3, 20, 52, 60, 99, 434]

    print("Descending Sorting -----")
    print(selectionSort(test, False))
    # [434, 99, 60, 52, 20, 3, -1, -5, -11, -200]


if __name__ == "__main__":
    main()
