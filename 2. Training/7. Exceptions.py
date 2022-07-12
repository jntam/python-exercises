import sys

try:
    print(sys.argv[1])
except IndexError as e:
    print(e)
    print('Not enough parameters.')
# 当有多种可能的异常可以用except对每一种错误分别进行处理，或
# except Exception as r:
# print(r)
