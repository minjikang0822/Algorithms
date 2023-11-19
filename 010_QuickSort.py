def quickSort_A(target):
    if len(target) <= 1:
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
        if left < right and target[left] > target[right]:
            target[left], target[right] = target[right], target[left]
        else:
            break

        if left+1 >= right-1:
            break
        else:
            left += 1
            right -= 1
    if target[right] < pivot:
        target[pivot_idx], target[right] = target[right], target[pivot_idx]
        pivot_idx = right

    return quickSort_A(target[:pivot_idx]) + [pivot] + quickSort_A(target[pivot_idx+1:])


def quickSort_D(target):
    print("target: ", target)
    if len(target) <= 1:
        return target
    pivot_idx = 0
    pivot = target[pivot_idx]

    left = 1
    right = len(target)-1
    while left < right:
        for i in range(left, len(target), 1):
            if target[i] < pivot:
                left = i
                break
        for j in range(right, 0, -1):
            if target[j] > pivot:
                right = j
                break
        if left <= right and target[left] < pivot < target[right]:
            target[left], target[right] = target[right], target[left]
        left += 1
        right -= 1
    if target[right] > pivot:
        target[pivot_idx], target[right] = target[right], target[pivot_idx]
        pivot_idx = right
    print("pivot_idx: ", pivot_idx, " pivot: ", pivot)
    print("new: ", target)
    print("left: ", target[:pivot_idx])
    print("right: ", target[pivot_idx+1:])
    return quickSort_D(target[:pivot_idx]) + [pivot] + quickSort_D(target[pivot_idx+1:])


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

