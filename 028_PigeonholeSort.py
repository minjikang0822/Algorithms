def pigeonholeSort(target):
    target_min = min(target)
    target_max = max(target)
    target_range = target_max - target_min + 1
    pigeonholes = [[] for _ in range(target_range)]

    for item in target:
        temp_idx = item - target_min
        pigeonholes[temp_idx].append(item)

    i = 0
    for hole in pigeonholes:
        if len(hole) != 0:
            while hole:
                target[i] = hole.pop(0)
                i += 1
    return target


def main():
    target = [-3, -11, 1, 0, 9, -3, 4, 6, 8, 8]
    print(pigeonholeSort(target))
    # [-11, -3, -3, 0, 1, 4, 6, 8, 8, 9]


if __name__ == "__main__":
    main()
