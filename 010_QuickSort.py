def quickSort(target):
    if len(target) == 1:
        return target

    pivot_idx = 0
    pivot = target[pivot_idx]
    left = 1
    right = len(target)-1

    while left < right:
        for i in range(left, len(target), 1):
            if target[i] > pivot:
                left = i
                break
        for j in range(right, 0, -1):
            if target[j] < pivot:
                right = j
                break

        print("left: ", left, " right: ", right)

        target[left], target[right] = target[right], target[left]
        left += 1
        right -= 1

    target[right], target[pivot_idx] = target[pivot_idx], target[right]
    return quickSort(target[:left]) + [pivot] + quickSort(target[right+1:])


def main():
    init = [9, 2, 1, 5, 4, 0, 3, 8, 7, 6]

    print("Ascending Sorting -----")
    print(quickSort(init))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Descending Sorting -----")
    print(quickSort(init))
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


if __name__ == "__main__":
    main()

