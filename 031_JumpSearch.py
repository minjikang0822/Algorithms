import math


def jumpSearch(arr, to_find):
    n = len(arr)
    block = int(math.sqrt(n))
    print(block)
    i = 0
    while arr[block * i] < to_find:
        i += 1
        if block * i > n:
            return -1

    idx = i
    while idx < block * (i + 1) < n:
        if arr[idx] == to_find:
            return idx
        idx += 1

    return -1


def main():
    test_arr = [-12, -8, -4, -3, -1, 0, 5, 6, 7, 10, 11]
    print(jumpSearch(test_arr, 6))


if __name__ == "__main__":
    main()
