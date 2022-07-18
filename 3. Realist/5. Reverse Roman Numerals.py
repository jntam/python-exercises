from typing import List


def value(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return None


def from_roman_numeral(roman_numeral: str):
    value_list: List[int] = []
    roman_list = list(roman_numeral)
    # print(roman_list)
    for i, letter in enumerate(roman_list):
        value_list.append(value(letter))

    for i in range(len(value_list) - 1):
        if value_list[i] < value_list[i+1]:
            value_list[i] *= -1
    # print(value_list)
    return sum(value_list)


if __name__ == '__main__':
    print(from_roman_numeral("MMMM"))

