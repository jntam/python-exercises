# for i in range(1000 + 1):
#     if i % 7 == 0:
#         n = 0
#         for j in str(i):
#             n += int(j)
#         if n % 3 == 0:
#             print(i)

# ---------
# for i in range(1000 + 1):
#     if i % 7 == 0:
#         numbers = [int(j) for j in str(i)]
#         # numbers = map(int, str(i))
#         n = sum(numbers)
#         if n % 3 == 0:
#             print(i)


# -------------
def is_divisible(num: int):
    if num % 7 == 0:
        numbers = [int(j) for j in str(num)]
        n = sum(numbers)
        if n % 3 == 0:
            return True
    else:
        return False


for i in range(1000 + 1):
    if is_divisible(i):
        print(i)
