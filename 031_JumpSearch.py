import math


def jumpSearch(arr, to_find):
    n = len(arr)
    # size of block
    m = int(math.sqrt(n))

    k = 0
    while k * m < n:
        idx = k * m

        if arr[idx] == to_find:
            return idx

        elif arr[idx] > to_find:
            temp_idx = (k-1) * m
            while temp_idx < idx:
                if arr[temp_idx] == to_find:
                    return temp_idx
                temp_idx += 1
            break
        k += 1
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


if __name__ == "__main__":
    main()
