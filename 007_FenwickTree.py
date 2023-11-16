# Known as Binary Indexed Tree
print(bin(10))
print(format(10, 'b'))  # type => str
print(9 & -2)


# int & int -> AND operation between their binary values


def createFenwickTree(original_list, n):
    print("what")
    fenwick_list = [0] * (n + 1)
    temp = [0] * (n+1)
    for i in range(1, n + 1, 1):
        # idx for original_list
        j = i-1
        # AND Operation: both 1 at the same digit would return 1 else 0
        m = i & -i
        temp[i] = m
        if m == 1:
            fenwick_list[i] = original_list[j]
        elif m == 2:
            fenwick_list[i] = fenwick_list[i-1] + original_list[j]
        else:
            # we need to sum m elements
            # except the i th element, it would be m-1 elements
            # -> need sum of elements from i-1-(m-1)th to i-1 th
            # --> i-1-(m-1) = i-1-m+1 = i-m
            sum_before_i = fenwickSum(fenwick_list, i-m, i-1)
            fenwick_list[i] = sum_before_i + original_list[j]
    print(temp[1:])
    return fenwick_list[1:]


def fenwickSum(fenwick_list, start, end):
    result = 0
    i = end
    print(start)
    while i > start:
        result += fenwick_list[i]
        i -= i & -i
    return result


def main():
    test_list = [5, 2, 9, -3, 5, 20, 10, -7, 2, 3, -4, 0, -2, 15, 5]
    print("Fenwick Tree")
    fenwickTree = createFenwickTree(test_list, len(test_list))
    print(fenwickTree)


if __name__ == "__main__":
    main()
