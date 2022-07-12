def collatz_length(n: int):
    collatz = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        elif n % 2 == 1:
            n = 3 * n + 1
        collatz.append(n)
    return len(collatz)


if __name__ == '__main__':
    print(collatz_length(10))
