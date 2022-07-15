from typing import List


def generate_row(num_row: int):
    row_list: List[int] = []
    tem = [1]
    if num_row == 0:
        return tem
    else:
        for i in range(num_row):
            tem.insert(0, 0)
            tem.append(0)
            row_list: List[int] = []
            for j in range(len(tem) - 1):
                row_list.append(tem[j] + tem[j + 1])
            tem = row_list[:]
        return row_list


def print_pascal_triangle(height: int):
    row_lists: List[List[str]] = []
    for num_row in range(height):
        row_list = generate_row(num_row)
        row_list = [str(x) for x in row_list]
        row_lists.append(row_list)
        print(" ".join(row_list))


if __name__ == '__main__':
    print_pascal_triangle(5)
