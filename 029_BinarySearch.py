def binarySearch(sorted_arr, to_find):
    n = len(sorted_arr) - 1
    start = 0
    mid = n//2
    end = n

    while 0 <= mid <= n:
        if sorted_arr[mid] > to_find:
            end = mid
            mid = mid//2
        elif sorted_arr[mid] < to_find:
            start = mid
            mid = (end - start) // 2
        else:
            return mid

    # item not found
    return -1


def main():
    pass


if __name__ == "__main__":
    main()
