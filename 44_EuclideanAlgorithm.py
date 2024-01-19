def gcd(num1, num2):
    A, B = max(num1, num2), min(num1, num2)

    if A % B == 0:
        return A

    R = A % B
    return gcd(B, R)


def main():
    print(gcd(192, 162))
    # 12


if __name__ == "__main__":
    main()
