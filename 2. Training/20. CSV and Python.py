import csv
import datetime
import time
import typing


def generate_csv(a_list: typing.List[tuple]):
    # 分离数据
    keys = []
    row = [[], []]
    for i in range(len(a_list)):
        for j in a_list[i]:

            keys.append(j[0])
            row[i].append(j[-1])
            if isinstance(row[i][-1], tuple):
                row[i][-1] = ",".join(list(row[i][-1]))
                # print()
            if isinstance(row[i][-1], datetime.date):
                a = row[i][-1]
                date = time.strptime(str(a), "%Y-%m-%d")
                row[i][-1] = time.strftime("%m/%d/%Y", date)

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


def parse_csv():
    with open('students.csv', newline='') as csv_f:
        reader = csv.DictReader(csv_f)
        # 提取数据

        marks = []
        dates = []
        number_of_row = 0  # 行数
        firstnames = []
        val = [[] for x in range(5)]
        keys = reader.fieldnames
        # 处理数据
        for row in reader:
            firstname = row['Firstname']
            val[number_of_row].append(firstname)
            # print(str(keys[number_of_row])
            mark = [int(x) for x in row['Marks'].split(",")]
            marks.append(mark)

            date = time.strftime("%Y,%m,%d", time.strptime(row['Birthdate'], "%m/%d/%Y")).split(",")
            date = [int(x) for x in date]
            dates.append(date)
            number_of_row += 1
        print(marks, firstnames, val)
        print(dates, number_of_row)

        # 字典list

        print(keys)
        dic = [{} for x in range(number_of_row)]
        # for key in keys:
        #     for num in range(number_of_row):
        #     dic[num][key] =
        print(dic)


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

    parse_csv()
