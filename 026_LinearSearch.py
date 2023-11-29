def linearSearch(target_list, what_to_find):
    for i in range(len(target_list)):
        if target_list[i] == what_to_find:
            print(what_to_find, "found at index", i)
            return i
    print(what_to_find, "not in the list")
    return -1


def main():
    target_list = [2, -2, 10, 9, 22, 5, 6, 15, 99, 45, 69, 32]
    linearSearch(target_list, 1)
    # 1 not in the list
    linearSearch(target_list, 99)
    # 99 found at index 8


if __name__ == "__main__":
    main()
