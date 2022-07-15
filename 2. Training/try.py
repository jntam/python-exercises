
import csv
import datetime
import time
from typing import List, Tuple, Dict
import pandas as pd
print(pd.__version__)


def generate_csv_row(row: Tuple[Tuple[str, int], Tuple[str, datetime.date], Tuple[str, Tuple[str, str]], Tuple[str, str]]):
    fieldnames: List[str] = []

    row_dict: Dict[str, any] = {}
    for cell in row:
        col_name = cell[0]
        value = cell[-1]

        if isinstance(value, tuple):
            value = ",".join(list(value))
        elif isinstance(value, datetime.date):
            d = time.strptime(str(value), "%Y-%m-%d")
            value = time.strftime("%m/%d/%Y", d)

        fieldnames.append(col_name)
        row_dict[col_name] = value

    return fieldnames, row_dict


def generate_csv(row_list: List[Tuple[Tuple[str, int], Tuple[str, datetime.date], Tuple[str, Tuple[str, str]], Tuple[str, str]]]):
    # 处理数据为字典
    fieldnames = []
    row_dict_list: List[Dict[str, any]] = []
    for i, row in enumerate(row_list):
        _fieldnames, row_dict = generate_csv_row(row)
        if i == 0:
            fieldnames = _fieldnames

        row_dict_list.append(row_dict)

    # 写入字典到结果文件
    with open('results.csv', 'w', newline='') as csv_f:
        write = csv.DictWriter(csv_f, fieldnames=fieldnames)
        write.writeheader()

        for row_dict in row_dict_list:
            write.writerow(row_dict)


if __name__ == '__main__':
    meteo = [(('temperature', 42),
              ('date', datetime.date(2017, 1, 22)),
              ('locations', ('Berlin', 'Paris')),
              ('weather', 'sunny')),
             (('temperature', -42),
              ('date', datetime.date(2017, 1, 22)),
              ('locations', ('Marseille', 'Moscow')),
              ('weather', 'cloudy'))]
    # generate_csv(meteo, 'results.csv')
