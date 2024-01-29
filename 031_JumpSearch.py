import math


def jumpSearch(arr, to_find):
    n = len(arr)
    block = int(math.sqrt(n))

    k = 0
    while arr[block * (k+1)] < to_find:
        k += 1
        if block * (k+1) > n:
            return -1

    idx = k
    while idx < block * (k + 1) < n:
        if arr[idx] == to_find:
            return idx
        idx += 1

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
    print(jumpSearch(test_arr, 10))


if __name__ == "__main__":
    main()
