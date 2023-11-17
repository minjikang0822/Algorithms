# Ascending
def selectionSort_A(to_sort):
    for i in range(len(to_sort)):
        min_idx = i
        for j in range(i+1, len(to_sort), 1):
            if to_sort[min_idx] > to_sort[j]:
                min_idx = j
        to_sort[i], to_sort[min_idx] = to_sort[min_idx], to_sort[i]


# Descending
def selectionSort_D(to_sort):
    for i in range(len(to_sort)):
        max_idx = i
        for j in range(i + 1, len(to_sort), 1):
            if to_sort[max_idx] < to_sort[j]:
                max_idx = j
        to_sort[i], to_sort[max_idx] = to_sort[max_idx], to_sort[i]


def main():
    init = [9, 2, 1, 5, 4, 0, 3, 8, 7, 6]
    print("Ascending Sorting -----")
    selectionSort_A(init)
    print(init)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Descending Sorting -----")
    selectionSort_D(init)
    print(init)
    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


if __name__ == "__main__":
    main()
