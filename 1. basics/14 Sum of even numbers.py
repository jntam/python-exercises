# 由于13题中的函数目的是输出[start, stop]中的所有偶数，与14题要求不同
# 13可以做如下修改
def is_even_numbers(n: int):
    if n % 2 != 1:
        return True


# def print_even_numbers(start: int, stop: int):
#     for i in range(start, stop):
#         if is_even_numbers(i) is True:
#             print(i)
# ---------------------------------------

# 以下是14题的答案，调用is_even_numbers函数
# Sum of even numbers <= 100
sum_of_even_numbers = 0
start = 0
stop = 100
for i in range(start, stop + 1):
    if is_even_numbers(i):
        sum_of_even_numbers += i
print(sum_of_even_numbers)
