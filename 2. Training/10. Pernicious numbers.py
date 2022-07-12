import prime


# 转换二进制
# def base_2(n: int):
#     b = []
#     while True:
#         q = n // 2
#         r = n % 2
#         b.append(r)
#         if q == 0:
#             break
#         n = q
#     b.reverse()
#     return b
#
#
# for i in range(222281, 222381):
#     base2 = base_2(i)
#     if prime.is_prime(sum(base2)):
#         print(i)

# ------------
for i in range(222281, 222381):
    a = "{0:b}".format(i)
    #
    numbers = [int(j) for j in a]
    n = sum(numbers)
    #
    # n = 0
    # for j in a:
    #     if j == '1':
    #         n += 1
    #
    if prime.is_prime(n):
        print(i)
