def ternarySearch(target, to_find):
    if len(target) < 2:
        print(to_find, "does not exists")
        return -1
    l = 0
    r = len(target) - 1
    m1 = l + (r - l) // 3
    m2 = r - (r - l) // 3

    if target[m1] == to_find:
        return m1
    elif target[m2] == to_find:
        return m2
    elif target[m1] > to_find:
        return ternarySearch(target[:m1], to_find)
    elif target[m2] < to_find:
        return ternarySearch(target[m2 + 1:], to_find)
    elif target[m1] < to_find < target[m2]:
        return ternarySearch(target[m1 + 1:m2], to_find)

def ternarySearch_withoutRecursion(target, to_find):
    l = 0
    r = len(target) - 1

    while l <= r:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3

        if target[m1] == to_find:
            return m1
        elif target[m2] == to_find:
            return m2
        elif target[m1] > to_find:
            r = m1 - 1
        elif target[m2] < to_find:
            l = m2 + 1
        elif target[m1] < to_find < target[m2]:
            l = m1 + 1
            r = m2 - 1
    print(to_find, "does not exists")
    return -1


def main():
    test_target = [-7, -3, 0, 2, 4, 7, 11, 20, 25, 34]
    print(ternarySearch(test_target, to_find=5))
    print("-------")
    print(ternarySearch_withoutRecursion(test_target, to_find=5))
    # 5 does not exists
    # -1
    print("************************")
    print(ternarySearch(test_target, to_find=11))
    print("-------")
    print(ternarySearch_withoutRecursion(test_target, to_find=11))
    # 6


if __name__ == "__main__":
    main()
