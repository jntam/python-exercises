from typing import List, Tuple


def sort_by_mark(mark_name_list: List[Tuple[int, str]]):
    return sorted(mark_name_list, reverse=True)


def sort_by_name(mark_name_list: List[Tuple[int, str]]):
    return sorted(mark_name_list, key=lambda name: name[1])


my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]

print(sort_by_mark(my_class))
print(sort_by_name(my_class))
