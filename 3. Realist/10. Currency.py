from typing import List, Dict


def how_to_pay(amount: int, currency: List[int]):
    pay_dict: Dict[int, int] = {}
    for value in sorted(currency, reverse=True):
        pay_dict[value] = amount // value
        amount = amount % value
    return pay_dict


if __name__ == "__main__":
    euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    print(how_to_pay(432, euro))
