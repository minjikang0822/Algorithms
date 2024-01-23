def fibonacciSearch(arr, to_find):
    n = len(arr)
    fibonacci_list = fibonacciNumbers(n)
    k = len(fibonacci_list)
    Fk = fibonacci_list[k]
    Fk1 = fibonacci_list[k-1]
    Fk2 = fibonacci_list[k-2]
    offset = -1
    idx = min(offset + Fk2, n-1)

    while arr[idx] != to_find:
        if arr[idx] > to_find:
            pass


def fibonacciNumbers(n):
    fibonacci_list = [0, 1]

    i = 2
    while fibonacci_list[-1] < n:
        fibonacci_list.append(fibonacci_list[i - 2] + fibonacci_list[i - 1])
        i += 1
    return fibonacci_list


def main():
    test_arr = [1, 2, 4, 5, 6, 10]
    fibonacciSearch(test_arr, 5)


if __name__ == "__main__":
    main()
