def sieveOfEratosthenes(n):
    # finding all prime numbers less than or equal to given n
    check_lst = [True for _ in range(n+1)]
    # 0 and 1 are not prime since prime number is greater than 1
    check_lst[0], check_lst[1] = False, False

    for i in range(len(check_lst)):
        if check_lst[i] is True:
            for j in range(2, n//i+1):
                not_prime_idx = i*j
                check_lst[not_prime_idx] = False

    prime_lst = [x for x in range(len(check_lst)) if check_lst[x] is True]
    return prime_lst


def main():
    print(sieveOfEratosthenes(26))
    # [2, 3, 5, 7, 11, 13, 17, 19, 23]

    print(sieveOfEratosthenes(50))
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


if __name__ == "__main__":
    main()