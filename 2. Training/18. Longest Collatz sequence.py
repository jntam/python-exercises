def collatz_length(n: int):
    le = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        le += 1
    return le


if __name__ == '__main__':
    print(collatz_length(10))
