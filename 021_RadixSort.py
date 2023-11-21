from collections import deque


def radixSort(target, is_ascending=True):
    digits = len(str(max(target)))
    buckets = [deque() for _ in range(10)]
    neg_list, pos_list = [], []

    for item in target:
        if item < 0:
            neg_list.append('0'*digits + str(-1*item))
        else:
            pos_list.append('0'*digits + str(item))

    lists = [neg_list, pos_list]
    for temp_list in lists:
        for i in range(-1, -1*digits-1, -1):
            for item in temp_list:
                digit_i = int(item[i])
                buckets[digit_i].append(item)
            j = 0
            for bucket in buckets if is_ascending else buckets[::-1]:
                # while there is an element in deque bucket
                while bucket:
                    temp_list[j] = bucket.popleft()
                    j += 1

    neg_list = list(map(lambda x: -1*int(x), neg_list))[::-1]
    pos_list = list(map(int, pos_list))

    answer = neg_list + pos_list if is_ascending else pos_list + neg_list

    return answer


def main():
    test = [39, 30, -30, 94, 200, -294, 2, 1, 0, -1, 85, 62, -11, -27, 395]
    print(radixSort(test))
    print(radixSort(test, False))


if __name__ == "__main__":
    main()
