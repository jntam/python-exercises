import string
from typing import List


def flatten(an_int_list: List[int]):
    cells = ''.join(w for w in str(an_int_list) if w not in string.punctuation)
    cells = cells.split()
    cells = [int(x) for x in cells]
    return cells


if __name__ == "__main__":
    print(flatten([[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]))
