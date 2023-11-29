def quickSort(bucket):
    if len(bucket) <= 1:
        return bucket
    pivot = bucket.pop(0)
    smaller_bucket = []
    larger_bucket = []
    for item in bucket:
        if item < pivot:
            smaller_bucket.append(item)
        else:
            larger_bucket.append(item)
    return quickSort(smaller_bucket) + [pivot] + quickSort(larger_bucket)


def bucketSort(target):
    n = len(target)
    buckets = [[] for _ in range(n)]

    for item in target:
        m = int(item * n)
        buckets[m].append(item)

    sorted_target = []
    for bucket in buckets:
        sorted_target += quickSort(bucket) if len(bucket) > 0 else bucket
    return sorted_target


def bucketSort_withNegativeNumbers(target):
    neg_list = []
    pos_list = []
    for item in target:
        if item < 0:
            neg_list.append(-1*item)
        else:
            pos_list.append(item)

    sorted_target = [-1*item for item in bucketSort(neg_list)[::-1]] + bucketSort(pos_list)
    return sorted_target


def main():
    target = [0.345, 0.1435, -0.352, -0.99, -0.9, 0, 0.145, 0.893, 0.3241]
    print(bucketSort_withNegativeNumbers(target))


if __name__ == "__main__":
    main()
