import itertools
import sys


# def is_prime(n: int):
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
import prime  # 7/1


start = 100000000
for j in itertools.count(start, 1):
    if prime.is_prime(j):
        print(j)
        sys.exit(0)
# -----------
num = 100000000
while prime.is_prime(num) is False:
    num += 1
print(num)
