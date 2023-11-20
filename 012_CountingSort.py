def countingSort(target, is_descending=False):
    counting_dict = {}
    for item in target:
        if item in counting_dict:
            counting_dict[item] += 1
        else:
            counting_dict[item] = 1

    answer = []
    for crr_key in sorted(counting_dict.keys(), reverse=is_descending):
        answer += [crr_key] * counting_dict[crr_key]
    return answer


def main():
    test = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    print("Ascending Sorting -----")
    print(countingSort(test))
    # [0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
    print("Descending Sorting -----")
    print(countingSort(test, True))
    # [9, 9, 8, 7, 6, 5, 5, 4, 3, 2, 2, 1, 1, 0, 0]


if __name__ == "__main__":
    main()