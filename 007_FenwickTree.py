# Known as Binary Indexed Tree
print(bin(10))
print(format(10, 'b'))  # type => str
print(9 & -2)


# int & int -> AND operation between their binary values
# Fenwick Tree index starts from 1

def createFenwickTree(original_list, n):
    fenwick_list = [0] * (n + 1)
    # temp list would have i & -i for ith value
    # it represents how many elements would we add up together to store at ith index of fenwickTree
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
            sum_before_i = fenwickSum(fenwick_list, i-1) - fenwickSum(fenwick_list, i-m)
            fenwick_list[i] = sum_before_i + original_list[j]
    # print(temp[1:])
    return fenwick_list


def fenwickSum(fenwick_list, i):
    result = 0
    while i > 0:
        result += fenwick_list[i]
        i -= i & -i
    return result


def fenwickUpdate(fenwick_list, i, to_add):
    while i < len(fenwick_list):
        fenwick_list[i] += to_add
        i += i & -i


def main():
    test_list = [5, 2, 9, -3, 5, 20, 10, -7, 2, 3, -4, 0, -2, 15, 5]
    print("Fenwick Tree")
    fenwickTree = createFenwickTree(test_list, len(test_list))
    print(fenwickTree[1:])
    # [5, 7, 9, 13, 5, 25, 10, 41, 2, 5, -4, 1, -2, 13, 5]
    print(fenwickSum(fenwickTree, 6))
    # 38
    fenwickUpdate(fenwickTree, 4, 10)
    print(fenwickTree[1:])
    # [5, 7, 9, 23, 5, 25, 10, 51, 2, 5, -4, 1, -2, 13, 5]


if __name__ == "__main__":
    main()
