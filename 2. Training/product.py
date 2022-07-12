from typing import Iterable


def mul(numbers: Iterable[int]):
    product = 1
    for number in numbers:
        product *= number
    return product

# print(mul([1,2,3]))
