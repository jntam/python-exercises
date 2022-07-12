from typing import Iterable, Callable


def filtered(obj: Iterable[int], lam: Callable[[int], bool]):  # ##
    return [x for x in obj if lam(x)]


def print_numbers(nums):
    print(', '.join([str(x) for x in nums]))


if __name__ == '__main__':
    items = [i for i in range(101)]

    mul_3 = filtered(items, lambda x: x % 3 == 0)
    print_numbers(mul_3)

    mul_5 = filtered(items, lambda x: x % 5 == 0)
    print_numbers(mul_5)

    mul_15 = filtered(items, lambda x: x % 15 == 0)
    print_numbers(mul_15)


# lam的类型我想指定为function（type(lambda...)=>class:'function'），但会报错
# lambda函数令我有点困惑
