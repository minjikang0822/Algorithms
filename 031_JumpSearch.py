import math


def jumpSearch(arr, to_find):
    n = len(arr)
    # size of block
    m = int(math.sqrt(n))

    k = 0
    while k * m < n and arr[k * m] <= to_find:
        k += 1

    idx = (k-1) * m
    for crr in range(m):
        crr_idx = min(idx + crr, n-1)
        if arr[crr_idx] == to_find:
            return crr_idx

    return -1


def main():
    test_arr = [-12, -8, -4, -3, -1, 0, 5, 6, 7, 10, 11]
    print(jumpSearch(test_arr, 6))
    # 7

    print(jumpSearch(test_arr, -6))
    # -1

    print(jumpSearch(test_arr, -12))
    # 0

    print(jumpSearch(test_arr, 11))
    # 10

    print(jumpSearch(test_arr, 10))
    # 9

    print(jumpSearch(test_arr, -8))
    # 1


if __name__ == "__main__":
    main()
