from typing import List


def generate_multiflavor_list(flavor_list: List[str]):
    for num1 in range(len(flavor_list)):
        for num2 in range(num1+1, len(flavor_list)):
            print("{}, {}".format(flavor_list[num1], flavor_list[num2]))


FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]
generate_multiflavor_list(FLAVORS)
