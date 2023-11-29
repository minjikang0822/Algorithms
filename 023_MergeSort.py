def mergeSort(target):
    if len(target) == 2:
        if target[0] > target[1]:
            return target[::-1]
        else:
            return target
    elif len(target) == 1:
        return target

    mid_idx = len(target) // 2
    left_temp = mergeSort(target[:mid_idx])
    right_temp = mergeSort(target[mid_idx:])
    # print(left_temp, right_temp)
    sorted_target = []

    while left_temp and right_temp:
        if left_temp[0] < right_temp[0]:
            sorted_target.append(left_temp.pop(0))
        else:
            sorted_target.append(right_temp.pop(0))
        # print(sorted_target)

    # if target list has odd number of elements,
    # there would be one element left either left_temp or right_temp
    # so add it at the end of the sorted list
    sorted_target += left_temp + right_temp
    return sorted_target


def main():
    target = [-1, 3, 20, -33, 40, 19, 23, 14, -99]
    print(mergeSort(target))
    # [-99, -33, -1, 3, 14, 19, 20, 23, 40]


if __name__ == "__main__":
    main()
