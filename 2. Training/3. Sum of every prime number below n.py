# def is_prime(n: int):
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
import prime  # 7/1


def sum_primes(n: int):
    s = 0
    if n > 2:
        for j in range(n):
            if prime.is_prime(j) :
                s += j
        return s
    else:
        return s


# 修改


print(sum_primes(10))
