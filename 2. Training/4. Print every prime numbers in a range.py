# def is_prime(n: int):
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
import prime  # 7/1


prime_number = []
range_min = 10000
range_max = 10050
for j in range(range_min, range_max+1):
    if prime.is_prime(j) :
        prime_number.append(str(j))
print(', '.join(prime_number))
