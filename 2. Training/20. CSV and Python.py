import csv
import datetime
import time
from typing import Dict, Optional, Sequence, List


def generate_csv(a_list: List[tuple]):
    # 分离数据
    keys = []
    row = [[], []]
    for i in range(len(a_list)):
        for j in a_list[i]:
            key = j[0]
            value = j[-1]

            if isinstance(value, tuple):
                value = ",".join(list(value))
            if isinstance(value, datetime.date):
                date = time.strptime(str(value), "%Y-%m-%d")
                value = time.strftime("%m/%d/%Y", date)

            keys.append(key)
            row[i].append(value)
    keys_s = list(set(keys))
    keys_s.sort(key=keys.index)

    # 字典
    dic = [{}, {}]
    for a in range(len(keys_s)):
        dic[0][keys_s[a]] = row[0][a]
        dic[1][keys_s[a]] = row[1][a]

    with open('results.csv', 'w', newline='') as csv_f:
        write = csv.DictWriter(csv_f, fieldnames=keys_s)
        write.writeheader()
        for row in range(len(dic)):
            write.writerow(dic[row])

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

        # 输出字典到结果列表
        print(row_dict_list)


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
    parse_csv()
