from typing import Tuple, List, Dict, Optional, Sequence, Union
import pandas as pd
import datetime
import time
from pandas import Series, DataFrame
from pandas.io.parsers import TextFileReader
# ------------------------exercise 1-----------------------------


def generate_csv_row(row: Tuple[Tuple[str, int], Tuple[str, datetime.date],
                                Tuple[str, Tuple[str, str]], Tuple[str, str]]):

    row_dict: Dict[str, any] = {}
    for cell in row:
        key = cell[0]
        value = cell[-1]

        if isinstance(value, tuple) or isinstance(value, list):
            value = ",".join(list(value))
        elif isinstance(value, datetime.date):
            d = time.strptime(str(value), "%Y-%m-%d")
            value = time.strftime("%m/%d/%Y", d)

        row_dict[key] = value

    return row_dict


def generate_csv(row_list: List[Tuple[Tuple[str, int], Tuple[str, datetime.date],
                                      Tuple[str, Tuple[str, str]], Tuple[str, str]]]):
    # 处理数据为字典
    row_dict_list: List[Dict[str, any]] = []
    for row in row_list:
        row_dict = generate_csv_row(row)

        row_dict_list.append(row_dict)

    # 写入csv文件
    df = pd.DataFrame(row_dict_list, index=None)
    df.to_csv('results_pd.csv', index=False)

# ------------------------exercise 2-----------------------------


def generate_row_dict(fieldnames: Optional[Sequence], row: any, df: Union[TextFileReader, Series, DataFrame, None]):
    row_dict: Dict[str, any] = {}
    for key in fieldnames:
        value = df.loc[row][key]
        # 格式化
        if key == 'Birthdate':
            struct_time = time.strptime(value, "%m/%d/%Y")
            value = datetime.date(struct_time.tm_year, struct_time.tm_mon, struct_time.tm_mday)
        elif key == 'Marks':
            value = [int(x) for x in value.split(",")]
        # 添加字典k_v
        row_dict[key] = value
    return row_dict


def parse_csv():
    # 读取csv
    df = pd.read_csv('students.csv')
    fieldnames = df.columns  # 列index
    reader = df.index  # 行index
    # print(fieldnames, '\n', reader)

    # 制作字典、并将字典储存到列表
    row_dict_list: List[Dict[str, any]] = []
    for row in reader:
        row_dict = generate_row_dict(fieldnames, row, df)
        row_dict_list.append(row_dict)

        # 返回字典到结果列表
    return row_dict_list


if __name__ == '__main__':
    meteo = [(('temperature', 42),
              ('date', datetime.date(2017, 1, 22)),
              ('locations', ('Berlin', 'Paris')),
              ('weather', 'sunny')),
             (('temperature', -42),
              ('date', datetime.date(2017, 1, 22)),
              ('locations', ('Marseille', 'Moscow')),
              ('weather', 'cloudy'))]
    generate_csv(meteo)
# ------------------------exercise 2-----------------------------
    print(parse_csv())
