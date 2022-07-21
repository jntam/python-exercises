from typing import List


def flatten(an_int_list: List):
    flatten_list = []
    for ele in an_int_list:
        if isinstance(ele, list):
            flatten_list.extend(flatten(ele))
        else:
            flatten_list.append(ele)
    return flatten_list


if __name__ == "__main__":
    print(flatten([[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]))
