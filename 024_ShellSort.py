def shellSort(target):
    h = len(target)//2
    while h > 0:
        # print(h)
        for i in range(h):
            for j in range(i, len(target), h):
                # same logic as insertion sort
                for k in range(j, i, -h):
                    if target[k] < target[k-h]:
                        target[k], target[k-h] = target[k-h], target[k]
                    else:
                        break
            # print(target)
        h = h//2
    return target


def main():
    target = [-20, 14, 99, 2, -1, 0, 11, 25, 24, 39, 30]
    print(shellSort(target))
    # [-20, -1, 0, 2, 11, 14, 24, 25, 30, 39, 99]


if __name__ == "__main__":
    main()
