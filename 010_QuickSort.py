def quickSort_A(target):
    if len(target) <= 1:
        return target
    pivot = target[0]

    left, right = 1, len(target)-1
    while left <= right:
        while left < len(target) and target[left] <= pivot:
            left += 1

        while right > 0 and target[right] >= pivot:
            right -= 1
        if left < right:
            target[left], target[right] = target[right], target[left]
        else:
            target[0], target[right] = target[right], target[0]
    return quickSort_A(target[:right]) + [pivot] + quickSort_A(target[right+1:])


def quickSort_D(target):
    if len(target) <= 1:
        return target
    pivot = target[0]

    left, right = 1, len(target) - 1
    while left <= right:
        while left < len(target) and target[left] >= pivot:
            left += 1

        while right > 0 and target[right] <= pivot:
            right -= 1
        if left < right:
            target[left], target[right] = target[right], target[left]
        else:
            target[0], target[right] = target[right], target[0]
    return quickSort_D(target[:right]) + [pivot] + quickSort_D(target[right + 1:])


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

