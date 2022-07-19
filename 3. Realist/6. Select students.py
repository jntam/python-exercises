from typing import List, Dict, Union


def select_student(students: List[List[Union[str, int]]], threshold: int):
    student_dict: Dict[str, List[List[Union[str, int]]]] = {}
    accepted_list: List[List[Union[str, int]]] = []
    refused_list: List[List[Union[str, int]]] = []

    for student in students:
        if student[1] < threshold:
            refused_list.append(student)
        else:
            accepted_list.append(student)

    student_dict['Accepted'] = sorted(accepted_list, key=lambda stu: stu[1], reverse=True)
    student_dict['Refused'] = sorted(refused_list, key=lambda stu: stu[1])

    return student_dict


if __name__ == "__main__":
    my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]
    print(select_student(my_class, 50))
