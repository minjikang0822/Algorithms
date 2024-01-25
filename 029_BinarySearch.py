def binarySearch(sorted_arr, to_find):
    left = 0
    right = len(sorted_arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        print("left:", left, "mid:", mid, "right:", right)
        if sorted_arr[mid] > to_find:
            right = mid
        elif sorted_arr[mid] < to_find:
            left = mid
        else:
            return mid

    # item not found
    return -1


def main():
    test_arr = [-10, -5, -2, -1, 0, 2, 4, 6, 12, 13, 14]

    print(binarySearch(test_arr, 12))
    # 8

    print(binarySearch(test_arr, -2))
    # 2


if __name__ == "__main__":
    main()
