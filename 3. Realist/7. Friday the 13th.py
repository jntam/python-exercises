import datetime


def friday_the_13th():
    today = datetime.date.today()

    if today.weekday() == 4 and today.day == 13:
        return today.strftime("%Y-%m-%d")

    year = today.year
    month = today.month
    day = 13
    if today.day > day:
        month += 1

    while True:
        dat = datetime.date(year, month, day)
        if dat.weekday() == 4:
            break

        month += 1
        if month == 13:
            year += 1
            month = 1

    return dat.strftime("%Y-%m-%d")


if __name__ == "__main__":
    print(type(friday_the_13th()))
    print(friday_the_13th())
