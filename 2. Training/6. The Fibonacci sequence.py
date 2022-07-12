def fibonacci(n: int):
    sequence = []
    i = 1
    while i <= n:
        if i <= 2:
            sequence.append(1)
        else:
            sequence.append(sequence[-2] + sequence[-1])
        i += 1
    return sequence


# 修改

# ---------递归函数（修改
def recursive_fibonacci(n: int):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        sequence = recursive_fibonacci(n - 1)
        sequence.append(sequence[-2] + sequence[-1])
        return sequence


print(recursive_fibonacci(16))
