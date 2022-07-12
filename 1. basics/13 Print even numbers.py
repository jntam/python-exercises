# def print_even_numbers(start, stop):
#    for i in range(start, stop):
#        if i % 2 != 1:
#            print(i)


# 6/30修改
# 由于13题中的函数目的是输出[start, stop]中的所有偶数，与14题要求不同
# 13可以做如下修改
def is_even_numbers(n: int):
    if n % 2 != 1:
        return True


def print_even_numbers(start: int, stop: int):
    for i in range(start, stop):
        if is_even_numbers(i) is True:
            print(i)
