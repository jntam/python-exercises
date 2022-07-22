def battery_charge(battery: int):
    n = round(battery / 10)
    print("[{}]".format(1*"❚"*n + 1*" "*(10-n)))
    print("{}%".format(battery))


if __name__ == "__main__":
    for i in range(101):
        battery_charge(i)
