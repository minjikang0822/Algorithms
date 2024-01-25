def fibonacciSearch(arr, to_find):
    n = len(arr)
    fibonacci_list = fibonacciNumbers(n)
    m = len(fibonacci_list) - 1
    offset = -1

    while fibonacci_list[m] > 1:
        Fm2 = fibonacci_list[m - 2]
        idx = min(offset + Fm2, n - 1)

        if arr[idx] > to_find:
            m = m - 2
        elif arr[idx] < to_find:
            m = m - 1
            offset = idx
        else:
            return idx

    return -1


def fibonacciNumbers(n):
    fibonacci_list = [0, 1]
    i = 2
    while fibonacci_list[-1] < n:
        fibonacci_list.append(fibonacci_list[i - 2] + fibonacci_list[i - 1])
        i += 1
    return fibonacci_list


def main():
    test_arr = [12, 14, 16, 17, 20, 24, 31, 43, 50, 62]
    idx1 = fibonacciSearch(test_arr, 24)
    print(idx1)
    # 5

    idx2 = fibonacciSearch(test_arr, 12)
    print(idx2)
    # 0

    idx3 = fibonacciSearch(test_arr, 62)
    print(idx3)
    # 9


if __name__ == "__main__":
    main()
