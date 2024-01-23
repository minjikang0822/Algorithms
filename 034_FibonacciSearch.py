def fibonacciSearch(arr):
    n = len(arr)


def fibonacciNumbers(n):
    fibonacci_list = [0, 1]

    i = 2
    while fibonacci_list[-1] < n:
        fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
        i += 1
    return fibonacci_list


def main():
    pass


if __name__ == "__main__":
    main()
