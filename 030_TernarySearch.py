def ternarySearch(target, to_find):
    if len(target) < 2:
        print(to_find, "does not exists")
        return -1
    l = 0
    r = len(target)-1
    m1 = l + (r - l) // 3
    m2 = r - (r - l) // 3
    print(target)
    print(m1)
    print(m2)
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


def main():
    test_target = [-7, -3, 0, 2, 4, 7, 11, 20, 25, 34]
    print(ternarySearch(test_target, to_find=5))


if __name__ == "__main__":
    main()
