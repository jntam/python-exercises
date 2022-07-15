import csv
import datetime
import time
from typing import Dict, Optional, Sequence, List, Tuple
# 为通过checker的答案
# 实际应用应该：参数类型、形参名称应该意义明确，便于使用者添加正确的参数；
#             输出的文件名称、读取的文件名称（可能）需要作为函数的一个参数，方便使用


def generate_csv_row(row: Tuple[Tuple[str, int], Tuple[str, datetime.date],
                                Tuple[str, Tuple[str, str]], Tuple[str, str]]):
    fieldnames: List[str] = []

    row_dict: Dict[str, any] = {}
    for cell in row:
        col_name = cell[0]
        value = cell[-1]

        if isinstance(value, tuple) or isinstance(value, list):
            value = ",".join(list(value))
        elif isinstance(value, datetime.date):
            d = time.strptime(str(value), "%Y-%m-%d")
            value = time.strftime("%m/%d/%Y", d)

        fieldnames.append(col_name)
        row_dict[col_name] = value

    return fieldnames, row_dict


def generate_csv(row_list: List[Tuple[Tuple[str, int], Tuple[str, datetime.date],
                                      Tuple[str, Tuple[str, str]], Tuple[str, str]]]):
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

# ------------------------exercise 2-----------------------------


def generate_row_dict(fieldnames: Optional[Sequence], row: csv.DictReader):
    row_dict: Dict[str, any] = {}
    for key in fieldnames:
        value = row[key]
        if key == 'Birthdate':
            struct_time = time.strptime(value, "%m/%d/%Y")
            value = datetime.date(struct_time.tm_year, struct_time.tm_mon, struct_time.tm_mday)
        elif key == 'Marks':
            value = [int(x) for x in value.split(",")]

        row_dict[key] = value
    return row_dict


def parse_csv():
    with open('students.csv', newline='') as csv_f:
        reader = csv.DictReader(csv_f)
        fieldnames = reader.fieldnames

        # 制作字典、并将字典储存到列表
        row_dict_list: List[Dict[str, any]] = []
        for row in reader:
            row_dict = generate_row_dict(fieldnames, row)
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
    # ----------------exercise 2--------------
    print(parse_csv())
